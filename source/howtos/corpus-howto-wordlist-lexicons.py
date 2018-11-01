#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import names, stopwords, words
print(words.fileids())
print(words.words('en')) # doctest: +ELLIPSIS
print(stopwords.fileids()) # doctest: +ELLIPSIS
print(stopwords.words('portuguese')) # doctest: +ELLIPSIS
print(names.fileids())
print(names.words('male.txt')) # doctest: +ELLIPSIS
print(names.words('female.txt')) # doctest: +ELLIPSIS

from nltk.corpus import cmudict
print(cmudict.entries()[653:659]) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
# Load the entire cmudict corpus into a Python dictionary:
transcr = cmudict.dict()
print([transcr[w][0] for w in 'Natural Language Tool Kit'.lower().split()]) 
