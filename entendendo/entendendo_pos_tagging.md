# words = read_from_file(filename)

# freq_words = FreqDist(words)
# freq_words_dict = freq_dict(words)

# should receive a a FreqDist object
# and will return all the keys in a list

# floresta treebank has a tagging scheme that needs to be simplyfied since
# it does not have [Universal Dependencies](http://universaldependencies.org/introduction.html)

# to train taggers we need to use whole sentences
# tsents = floresta.tagged_sents()
# tsents = [[(w.lower(),simplify_tag(t)) for (w,t) in sent] for sent in tsents if sent]
# train = tsents[100:]
# test = tsents[:100]


# defining a tagger that will say all token is a noun
# in the floresta corpus, after simplifying the tags, nouns are marked by 'n'
# default_tagger = DefaultTagger('n')

# # default_tagger working example:
# tokens = wt('Estado, e foi um dos amigos particulares do vice-rei Conde da Cunha.')
# default_tagger.tag(tokens)
# result should be as follows:
# [('Estado', 'n'),
#  (',', 'n'),
#  ('e', 'n'),
#  ('foi', 'n'),
#  ('um', 'n'),
#  ('dos', 'n'),
#  ('amigos', 'n'),
#  ('particulares', 'n'),
#  ('do', 'n'),
#  ('vice-rei', 'n'),
#  ('Conde', 'n'),
#  ('da', 'n'),
#  ('Cunha', 'n'),
#  ('.', 'n')]

# evaluating how does the default_tagger performs across already tagged words
# default_tagger.evaluate(tsents)
# 0.18919339916545513
# ele só acerta aproximadamente um quinto das palavras
# from the nltk book:
# Default taggers assign their tag to every single word, even words that have never been encountered before. As it happens, once we have processed several thousand words of English text, most new words will be nouns. As we will see, this means that default taggers can help to improve the robustness of a language processing system.

