#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import sys
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

class StopWords(object):
    def remove(self, string):
        if not string:
            string = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
        stopWords = set(stopwords.words('english'))
        words = word_tokenize(string)
        wordsFiltered = []

        for w in words:
            if w not in stopWords:
                wordsFiltered.append(w)

        return wordsFiltered
