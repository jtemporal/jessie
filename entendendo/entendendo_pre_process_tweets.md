



ideally we should set the data path were the data generated is stored
since it is not, lets do the easy fix
this should be received as args or just use sample set
maybe add an verification here, if data is present do nothing else copy

def copy_file(filename)

# terms of interest
# futher analysis should be automated
# terms = ['dengue', 'chikungunya', 'zika', 'microcefalia']

######## READING DATA #########
# tweets text
# method strings returns the text of the tweet in a list
# dengue_text = twitter_samples.strings('dengue-tweets-json')

######## PRE-PROCESSING ########
# map: aplies a function to a iterable
# map(lambda s: s.lower(), dengue_text)
# the line above will return a map object which is an iterable
# dengue_text = list(map(lambda tweet: tweet.lower(), dengue_text))

# some of the repeated tweets changed only a part of the link that was used \/
# 'mesmo no outono, casos de dengue em friburgo continuam aumentando: em uma semana surgiram 358 casos da doença... https://t.co/3lwrwahyp7',
# 'mesmo no outono, casos de dengue em friburgo continuam aumentando: em uma semana surgiram 358 casos da doença... https://t.co/yvevkwae64',
# 'mesmo no outono, casos de dengue em friburgo continuam aumentando: em uma semana surgiram 358 casos da doença... https://t.co/f5npoeastl',
# 'mesmo no outono, casos de dengue em friburgo continuam aumentando: em uma semana surgiram 358 casos da doença... https://t.co/fkgvgxcnwf',
# we need to replace the urls to something else, also a retweet from a retweet
# will have the same text apart from the user, hence the change for usernames
# let's replace, links, mentions and hashtags with a known term that will make
# easier to remove similar tweets and thoose terms can be added to stop words
# list: links -> 'URL', mentions -> 'AT_USER' and #hashtags -> hashtags
# hashtags may be part of the frase construction hence transforming it itself
# without the simbol

# testing = [
# '@pkcanadianbits obrigada por aparecer, é sobre saúde, eu quero falar sobre zika, dengue e a outra que eh dificil de escrver',
#  'isso aí é dengue minha senhora https://t.co/pxrtblsy7j',
#  'bom da dengue é que vou ficar 4 dias morrendo em casa, mal da dengue nao vou receber sexta :(',
#  'dengue é uma praga mesmo, pqp',
#  'trechos de seis bairros recebem inseticida contra o mosquito da dengue nesta quinta, na capital https://t.co/dppolwxxur']
# testing = replace_features(testing)
# print('replacing links, user names and hashtags')
# for text in tqdm(dengue_text):
#     i = dengue_text.index(text)
#     dengue_text[i] = replace_features(text)

# len(dengue_text)
# 1000
# len(set(dengue_text))
# 607

# removing repeated tweets
# dengue_text = list(set(dengue_text))



# save_to_file('dengue-text.txt', dengue_text)

# tokenize tweets text
# dengue_tokens = twitter_samples.tokenized('dengue-tweets-json')
# will return a list of lists of strings which are the tokens
# decided not to use this tokenizer once it tokenizes from the raw data and it
# will need to remove repeated tweets once more, so let's use the other
# tokenizer provided from nltk
# word_tokenize(s)
# the following function will give the same result as
# dengue_tokens = twitter_samples.tokenized('dengue-tweets-json')

# dengue_tokens = tokenize_tweets(dengue_text)

# using chain to 'unlist' dengue_tokens
# dengue_words = list(chain.from_iterable(dengue_tokens))

# pt stop words
# stop_words = stopwords.words('portuguese')

# punctuation: from string module
# imported from strings module
# personal list of stopwords
# my_stopwords = ['rt', 'dm', 'AT_USER', 'URL']

# print('appending stopwords')
# for word in tqdm(my_stopwords):
#     stop_words.append(word)
#
# new_words = [word for word in dengue_words if word.isalnum()]
# new_words = [word for word in new_words if word not in stop_words]

# print('writing words to file')
# save_to_file('words_list.txt', new_words)
# print('writing tweets to file')
# save_to_file('tweets_list.txt', dengue_text)

