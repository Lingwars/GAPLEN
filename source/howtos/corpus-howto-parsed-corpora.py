#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import treebank
print(treebank.fileids()) # doctest: +ELLIPSIS
print(treebank.words('wsj_0003.mrg'))
print(treebank.tagged_words('wsj_0003.mrg'))
print(treebank.parsed_sents('wsj_0003.mrg')[0])


from nltk.corpus import ptb
print(ptb.fileids()) # doctest: +SKIP


