#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import timit
print(timit.utteranceids()) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
item = timit.utteranceids()[5]
print(timit.phones(item)) # doctest: +NORMALIZE_WHITESPACE
print(timit.words(item))
timit.play(item) # doctest: +SKIP
for tree in timit.phone_trees(item):
    print(tree)

print(timit.phone_times(item)) # doctest: +ELLIPSIS
print(timit.word_times(item)) # doctest: +ELLIPSIS
print(timit.sent_times(item))

print(timit.play(item, 2190, 8804))

print(timit.spkrid(item))
print(timit.sentid(item))
print(timit.spkrinfo(timit.spkrid(item))) # doctest: +NORMALIZE_WHITESPACE
timit.utteranceids(spkrid=timit.spkrid(item))
