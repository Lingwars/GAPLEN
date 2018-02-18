#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from nltk.stem import *

# Unit tests for the Porter stemmer
stemmer = PorterStemmer()

plurals = ['caresses', 'flies', 'dies', 'mules', 'denied',
               'died', 'agreed', 'owned', 'humbled', 'sized',
               'meeting', 'stating', 'siezing', 'itemization',
               'sensational', 'traditional', 'reference', 'colonizer',
               'plotted']
singles = [stemmer.stem(plural) for plural in plurals]
print(' '.join(singles))  # doctest: +NORMALIZE_WHITESPACE

# Unit tests for Snowball stemmer

from nltk.stem.snowball import SnowballStemmer
print(" ".join(SnowballStemmer.languages))

stemmer = SnowballStemmer("english")
print(stemmer.stem("running"))

stemmer2 = SnowballStemmer("english", ignore_stopwords=True)
print(stemmer.stem("having"))

print(stemmer2.stem("having"))

print(SnowballStemmer("english").stem("generously"))
print(SnowballStemmer("spanish").stem("cuidados"))
# Spanish

plurales = ['cuidados', 'vuelos', 'muertes', 'mulas', 
            'muerto']
singulares = [stemmer.stem(plural) for plural in plurales]
print(' '.join(singulares))  # doctest: +NORMALIZE_WHITESPACE
