#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import subjectivity
print(subjectivity.categories())
print(subjectivity.sents()[23])
print(subjectivity.words(categories='subj'))
