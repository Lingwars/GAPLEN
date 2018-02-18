#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import comparative_sentences
comparison = comparative_sentences.comparisons()[0]
print(comparison.text)
print(comparison.entity_2)
print(comparison.feature, comparison.keyword)
print(len(comparative_sentences.comparisons()))
