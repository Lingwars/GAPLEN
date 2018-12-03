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

import unittest
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import inaugural
from nltk.corpus import gutenberg
from nltk.corpus import reuters
from nltk.corpus import cmudict

class TddInPythonExample(unittest.TestCase):

    # def test_new_corpus_returns_correct_result(self):
    #     corpus_root = '/usr/share/dict'
    #     wordlists = PlaintextCorpusReader(corpus_root, '.*')
    #     self.assertEqual(['README.select-wordlist', 'american-english', 'cracklib-small', 'words', 'words.pre-dictionaries-common'], wordlists.fileids())

    def test_corpus_fileids_method_returns_correct_result(self):
        fileids = inaugural.fileids()
        self.assertEqual(['1789-Washington.txt', '1793-Washington.txt', '1797-Adams.txt'], fileids[0:3])

    def test_corpus_sents_method_returns_correct_result(self):
        sents1 = [['[', 'Sense', 'and', 'Sensibility', 'by', 'Jane', 'Austen', '1811', ']'], ['CHAPTER', '1']]
        self.assertEqual(gutenberg.sents('austen-sense.txt')[0:2], sents1)

    def	test_corpus_categories_method_returns_correct_result(self):
        cat = reuters.categories()[0:2]
        self.assertEqual(cat, ['acq', 'alum'])

    def test_corpus_cmudict_method_returns_correct_result(self):
        transcr = cmudict.dict()
        t = [transcr[w][0] for w in 'Natural Language Tool Kit'.lower().split()]
        self.assertEqual(t, [['N', 'AE1', 'CH', 'ER0', 'AH0', 'L'], ['L', 'AE1', 'NG', 'G', 'W', 'AH0', 'JH'], ['T', 'UW1', 'L'], ['K', 'IH1', 'T']])
