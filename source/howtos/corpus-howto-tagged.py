#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import brown
print(brown.words())
print(brown.tagged_words())
print(brown.sents()) # doctest: +ELLIPSIS
print(brown.tagged_sents()) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
print(brown.paras(categories='reviews')) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
print(brown.tagged_paras(categories='reviews')) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE


print(brown.tagged_sents(tagset='universal')) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
from nltk.corpus import conll2000, switchboard
print(conll2000.tagged_words(tagset='universal')) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
