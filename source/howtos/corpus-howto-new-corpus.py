#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
my_corpus = nltk.corpus.PlaintextCorpusReader('/home/davidam/nltk_data/corpora/elpais', '.*\.ES')
print(my_corpus.sents('20180130-17h51m-9-ES')[0])

