from logging import INFO, basicConfig, info
from pickle import dump
from nltk import BigramTagger, DefaultTagger, TrigramTagger, UnigramTagger
from nltk.corpus import floresta, mac_morpho
from jessie import pos_tagging as pt


def simplify_tag(t):
    if "+" in t:
        return t[t.index("+")+1:]
    else:
        return t


def simplified_sents_floresta(tsents):
    return [[(w.lower(), simplify_tag(t)) for (w, t) in sent] for sent in tsents if sent]


def default_tagger_corpus(corpus):
    if corpus == 'floresta':
        return DefaultTagger('n')
    if corpus == 'macmorpho':
        return DefaultTagger('N')


def no_backoff_taggers(test, train, corpus='floresta'):
    default_tagger = default_tagger_corpus(corpus)

    info('training {} taggers without backoff'.format(corpus))
    info('this may take a while...\n')

    info(default_tagger)
    default_score = default_tagger.evaluate(test)
    print('accuracy score: {}\n'.format(default_score))

    # unigram tagger
    uni_tagger = UnigramTagger(train)
    # bigram tagger
    bi_tagger = BigramTagger(train)
    # trigram tagger
    tri_tagger = TrigramTagger(train)

    info(uni_tagger)
    uni_score = uni_tagger.evaluate(test)
    print('accuracy score: {}\n'.format(uni_score))

    info(bi_tagger)
    bi_score = bi_tagger.evaluate(test)
    print('accuracy score: {}\n'.format(bi_score))

    info(tri_tagger)
    tri_score = tri_tagger.evaluate(test)
    print('accuracy score: {}\n'.format(tri_score))


def backoff_taggers(test, train, save, corpus='floresta'):
    default_tagger = default_tagger_corpus(corpus)
    info('training {} taggers with backoff'.format(corpus))
    info('this may take a while...\n')

    info(default_tagger)
    default_score = default_tagger.evaluate(test)
    print('accuracy score: {}\n'.format(default_score))

    # UNIGRAM TAGGER WITH BACKOFF
    uni_tagger_backoff = UnigramTagger(train, backoff=default_tagger)

    # BIGRAM TAGGER WITH BACKOFF
    bi_tagger_backoff = BigramTagger(train, backoff=uni_tagger_backoff)

    # TRIGRAM TAGGER WITH BACKOFF
    tri_tagger_backoff = TrigramTagger(train, backoff=bi_tagger_backoff)

    info(uni_tagger_backoff)
    uni_backoff_score = uni_tagger_backoff.evaluate(test)
    print('accuracy score: {}\n'.format(uni_backoff_score))

    info(bi_tagger_backoff)
    bi_backoff_score = bi_tagger_backoff.evaluate(test)
    print('accuracy score: {}\n'.format(bi_backoff_score))

    info(tri_tagger_backoff)
    tri_backoff_score = tri_tagger_backoff.evaluate(test)
    print('accuracy score: {}\n'.format(tri_backoff_score))

    if not save:
        return

    accuracy_dict = {}
    accuracy_dict['uni'] = uni_backoff_score
    accuracy_dict['bi'] = bi_backoff_score
    accuracy_dict['tri'] = tri_backoff_score

    # Saving our Trigram-tagger with backoff
    if uni_backoff_score == max(accuracy_dict.values()):
        tagger_file = '{}_unigram_tagger_backoff.pkl'.format(corpus)
        output = open(tagger_file, 'wb')
        dump(uni_tagger_backoff, output, -1)
    elif bi_backoff_score == max(accuracy_dict.values()):
        tagger_file = '{}_bigram_tagger_backoff.pkl'.format(corpus)
        output = open(tagger_file, 'wb')
        dump(bi_tagger_backoff, output, -1)
    elif tri_backoff_score == max(accuracy_dict.values()):
        tagger_file = '{}_trigram_tagger_backoff.pkl'.format(corpus)
        dump(tri_tagger_backoff, output, -1)
    output.close()
    info('saving %s...\n', tagger_file)


def accuracy_measure():
    basicConfig(format='%(levelname)s %(message)s', level=INFO)
    info('reading tagged sentences')
    info('simplifying tags')

    # tagged sentences
    flo_tsents = simplified_sents_floresta(floresta.tagged_sents())
    mac_tsents = mac_morpho.tagged_sents()

    # FLORESTA test and train data
    flo_size = int(len(flo_tsents) * 0.9)
    flo_train = flo_tsents[:flo_size]
    flo_test = flo_tsents[flo_size:]

    # MAC MORPHO test and train data
    mac_size = int(len(mac_tsents) * 0.9)
    mac_train = mac_tsents[:mac_size]
    mac_test = mac_tsents[mac_size:]

    no_backoff_taggers(flo_test, flo_train)
    no_backoff_taggers(mac_test, mac_train, corpus='macmorpho')

    if not pt.check_for_taggers():
        save=True
    else:
        save=False

    backoff_taggers(flo_test, flo_train, save)
    backoff_taggers(mac_test, mac_train, save, corpus='macmorpho')

if __name__ == '__main__':
    accuracy_measure()
