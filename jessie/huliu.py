from jessie import pre_process_tweets as pp, pos_tagging as pt
import nltk
from pickle import load


def load_tagger(tagger_file):
    input = open(tagger_file, 'rb')
    tagger = load(input)
    input.close()
    return tagger

def hu_liu(filename='tweets_list_dengue_tweets_json.txt',
           tagger_pkl='trigram_tagger_backoff.pkl'):
    tweets = pt.read_from_file('tweets_list_dengue_tweets_json.txt')
    # http://www.linguateca.pt/floresta/BibliaFlorestal/anexo1.html
    # pron-pers   pronome pessoal
    # pron-det    pronome determinativo
    # pron-indp   pronome independente (com comportamento semelhante ao nome)
    grammar = r"""
        NP:
           {<pron-det|pron-pers|pron-indp|>?<adj>*<n>+}
           {<prop>+}
    """
    cp = nltk.RegexpParser(grammar)

    tagger = load_tagger('trigram_tagger_backoff.pkl')
    tagged = tagger.tag(nltk.word_tokenize(tweets[0]))

    result = cp.parse(tagged)
    result.draw()

if __name__ == '__main__':
    hu_liu()
