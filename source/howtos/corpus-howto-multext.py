#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
print(nltk.corpus.multext_east.words("oana-en.xml"))
print(nltk.corpus.multext_east.tagged_words("oana-en.xml"))
print(nltk.corpus.multext_east.tagged_sents("oana-en.xml", "universal"))
