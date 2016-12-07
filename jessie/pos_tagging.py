# coding: utf-8
from os import listdir
from re import compile, search
from logging import INFO, basicConfig, info
from pickle import dump, load

from jessie import pre_process_tweets as pp


def read_from_file(filename):
    lines = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            lines.append(line.replace('\n', ''))
            line = f.readline()
    info('{} lines were read from {}'.format(len(lines), filename))
    return lines


def load_tagger_from_pkl(tagger_filename):
    # tagger_filename = 'trigram_tagger_backoff.pkl'
    input = open(tagger_filename, 'rb')
    tagger = load(input)
    input.close()
    return tagger


def write_nouns_to_file(result, corpus, tag, filename):
    words = []
    for r in result:
        if r[1] == tag:
            words.append(r[0])

    print('\nwriting nouns to file...')

    if len(str.split(filename, '/')) > 1:
        filename = str.split(filename, '/')[len(str.split(filename, '/')) - 1]

    pp.save_to_file('{}_nouns_{}'.format(corpus, filename), words)


def check_for_taggers():
    taggers = []
    pkl = compile('gram_tagger')
    for item in listdir():
        if pkl.search(item):
            taggers.append(item)
    return taggers


def write_semicolon_nouns(tokens_list, tagger, corpus, corpus_tag, filename):
    nouns_per_tweet = []
    result_csv = []
    for tokens in tokens_list:
        nouns_per_tweet.append(tagger.tag(tokens))

    for itens in nouns_per_tweet:
        aux = []
        for item in itens:
            if corpus_tag in item:
                aux.append(item[0])
        result_csv.append(';'.join(aux))
    pp.save_to_file('{}_semicolon_{}'.format(corpus, filename), result_csv)


def pos_tagging(filename='tweets_list_dengue_tweets_json.txt'):
    basicConfig(format='%(levelname)s %(message)s', level=INFO)
    info('checking for taggers...')
    taggers = check_for_taggers()

    text = read_from_file(filename)
    tokens_list = pp.tokenize_tweets(text)

    info('loading taggers...\n')
    for t in taggers:
        tagger = load_tagger_from_pkl(t)
        result = tagger.tag(pp.unchain_list(tokens_list))
        # pp.save_to_file('{}_nouns_{}'.format(corpus, filename), words)
        corpus = str.split(t, '_')[0]
        if corpus == 'floresta':
            corpus_tag = 'n'
        elif corpus == 'macmorpho':
            corpus_tag = 'N'
        write_nouns_to_file(result, corpus, corpus_tag, filename)
        write_semicolon_nouns(tokens_list, tagger, corpus, corpus_tag, filename)


if __name__ == '__main__':
    pos_tagging()
