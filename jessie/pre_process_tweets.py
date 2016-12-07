# coding: utf-8
from itertools import chain
from logging import INFO, basicConfig, info
from os import system as sys
from os.path import abspath
from re import compile, sub

from nltk.corpus import stopwords, twitter_samples
from nltk.tokenize import word_tokenize


def copy_file(filename):
    """Will copy your data file to NLTK root data file

    :filename: file to to be copied e.g. 'sample-file'
    """

    nltk_data_path = '~/nltk_data/corpora/twitter_samples/'
    info('copiando {}'.format(filename))
    sys('cp {} {}'.format(abspath(filename), nltk_data_path))


def replace_features(tweet):
    # Convert www.* or https?://* to URL
    url = compile('((www\.[^\s]+)|(https?:/[^\s]+))')
    # Convert @username to AT_USER
    at_user = compile('@[^\s]+')
    # Replace #word with word
    mention = compile(r'#([^\s]+)')
    if url.search(tweet):
        tweet = sub(url, 'URL', tweet)
    if at_user.search(tweet):
        tweet = sub(at_user, 'joão', tweet)
    if mention.search(tweet):
        tweet = sub(mention, r'\1', tweet)

    return tweet


def save_to_file(filename, texts):
    info('saving data to file: %s', filename)
    with open(filename, 'w') as f:
        for text in texts:
            f.write(text)
            f.write('\n')


def read_from_file(filename):
    lines = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            lines.append(line.replace('\n', ''))
            line = f.readline()
    info('{} lines were read from {}'.format(len(lines), filename))
    return lines


def tokenize_tweets(tweets):
    tweets_tokens = []
    for tweet in tweets:
        tweets_tokens.append(word_tokenize(tweet))
    return tweets_tokens


def unchain_list(chained_list):
    return list(chain.from_iterable(chained_list))


def create_bag_of_words(words, my_stopwords=['rt', 'dm', 'URL']):
    stop_words = stopwords.words('portuguese')

    for word in my_stopwords:
        stop_words.append(word)

    new_words = [word for word in words if word.isalnum()]
    new_words = [word for word in new_words if word not in stop_words]
    new_words = [word for word in new_words if len(word) > 3]
    return new_words


def pre_process(filename='dengue_tweets_json'):
    basicConfig(format='%(levelname)s %(message)s', level=INFO)
    copy_file(filename)
    file_extensions = str.split(filename, '.')
    if len(file_extensions) > 1:
        dengue_text = read_from_file(filename)
    else:
        dengue_text = twitter_samples.strings(filename)
    dengue_text = list(map(lambda tweet: tweet.lower(), dengue_text))

    info('replacing links, user names and hashtags')
    for text in dengue_text:
        i = dengue_text.index(text)
        dengue_text[i] = replace_features(text)
    dengue_text = list(set(dengue_text))

    dengue_tokens = tokenize_tweets(dengue_text)
    dengue_words = unchain_list(dengue_tokens)

    new_words = create_bag_of_words(dengue_words)

    save_to_file('words_list_{}.txt'.format(file_extensions[0]), new_words)

    my_stopwords = ['rt', 'dm', 'URL']
    new_tokens = []
    for token_list in dengue_tokens:
        tokens = [token for token in token_list if token not in my_stopwords]
        new_tokens.append(tokens)

    dengue_text = []
    for tokens in new_tokens:
        dengue_text.append(' '.join(tokens))

    save_to_file('tweets_list_{}.txt'.format(file_extensions[0]), dengue_text)

if __name__ == '__main__':
    pre_process()
