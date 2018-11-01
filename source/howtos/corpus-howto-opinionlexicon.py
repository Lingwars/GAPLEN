#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import opinion_lexicon
print(opinion_lexicon.words()[:4])
print(opinion_lexicon.negative()[:4])
print(opinion_lexicon.words()[0:10])
print(sorted(opinion_lexicon.words())[0:10])
