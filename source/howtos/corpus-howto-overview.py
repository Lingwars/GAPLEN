#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk.corpus
# The Brown corpus:

#Each corpus is accessed by means of a "corpus reader" object from nltk.corpus
print(str(nltk.corpus.brown).replace('\\\\','/'))
# The Penn Treebank Corpus:
print(str(nltk.corpus.treebank).replace('\\\\','/'))
# The Name Genders Corpus:
print(str(nltk.corpus.names).replace('\\\\','/'))
# The Inaugural Address Corpus:
print(str(nltk.corpus.inaugural).replace('\\\\','/'))
print(str(nltk.corpus.treebank.fileids())) # doctest: +ELLIPSIS
#print(str(nltk.corpus.inaugural.fileids()) # doctest: +ELLIPSIS
# Each corpus reader provides a variety of methods to read data from the corpus, depending on the format of the corpus.


from nltk.corpus import inaugural
print(inaugural.raw('1789-Washington.txt')) # doctest: +ELLIPSIS
print(inaugural.words('1789-Washington.txt'))
print(inaugural.sents('1789-Washington.txt')) # doctest: +ELLIPSIS
print(inaugural.paras('1789-Washington.txt')) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE

# 

l1 = len(inaugural.words('1789-Washington.txt'))
l2 = len(inaugural.words('1793-Washington.txt'))
l3 = len(inaugural.words(['1789-Washington.txt', '1793-Washington.txt']))
print('%s+%s == %s' % (l1, l2, l3))

print(len(inaugural.words()))

print(inaugural.readme())
