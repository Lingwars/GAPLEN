#!/usr/bin/python
#-*- coding: utf-8 -*-

from nltk import *
from nltk.sem import logic
logic._counter._value = 0

# INTRODUCTION

# The NLTK discourse module makes it possible to test consistency and redundancy of simple discourses, using theorem-proving and model-building from nltk.inference.

dt = DiscourseTester(['a boxer walks', 'every boxer chases a girl'])

dt.sentences()

dt.grammar() # doctest: +ELLIPSIS




