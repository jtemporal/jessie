from os import listdir
from re import compile, search
from logging import INFO, basicConfig
from nltk import FreqDist

from jessie import (pos_tagging as pt, pre_process_tweets as pp,
                       rm_accentuation as ra)


def words_for_wordcloud(corpus, frequencies, nouns):
    terms = []
    for frequency in frequencies:
        if frequency[1] >= 10:
            terms.append(frequency[0])

    words = []
    for noun in nouns:
        if noun in terms:
            words.append(noun)
    words =  ' '.join(words)
    pp.save_to_file('wordcloud_{}.txt'.format(corpus), words)


def check_for_nouns_files():
    nouns_files = []
    nouns = compile('nouns')
    for item in listdir():
        if nouns.search(item):
            nouns_files.append(item)
    return nouns_files


def post_processing(filename):
    nouns = pp.create_bag_of_words(pt.read_from_file(filename))
    nouns = ra.replace_accentuation(nouns)
    return nouns


def freq_baseline(wordcloud=False, venn=False):
    basicConfig(format='%(levelname)s %(message)s', level=INFO)
    nouns_files = check_for_nouns_files()
    for filename in nouns_files:
        nouns = post_processing(filename)

        freq = FreqDist(nouns)
        frequencies = freq.most_common()

        minimum_count = 10

        candidate_aspect_terms = []
        for_venn = []
        for frequency in frequencies:
            if frequency[1] >= minimum_count:
                string = '{}: {}'.format(frequency[0], frequency[1])
                for_venn.append(frequency[0])
                candidate_aspect_terms.append(string)

        corpus = str.split(filename, '_')[0]
        candidate_file = 'aspect_terms_{}'.format(filename)
        pp.save_to_file(candidate_file, candidate_aspect_terms)

        if venn:
            venn_file = 'venn_{}'.format(filename)
            pp.save_to_file(venn_file, for_venn)

        if wordcloud:
            words_for_wordcloud(corpus, frequencies, nouns)

if __name__ == '__main__':
    freq_baseline()
