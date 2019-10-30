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
from nltk.corpus import wordnet

class TddInPythonExample(unittest.TestCase):

    def test_syn_returns_correct_result(self):
        syns = wordnet.synsets("program")
        # An example of a synset:
        self.assertEqual(syns[0].name(), "plan.n.01")
        # Just the word:
        self.assertEqual(syns[0].lemmas()[0].name(), "plan")
        # Definition of that first synset:
        self.assertEqual(syns[0].definition(), "a series of steps to be carried out or goals to be accomplished")
        # Examples of the word in use in sentences:
        self.assertEqual(syns[0].examples(), ['they drew up a six-step plan', 'they discussed plans for a new bond issue'])

    def test_antonym_returns_correct_result(self):
        antonyms = []
        for syn in wordnet.synsets("good"):
            for l in syn.lemmas():
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
        self.assertEqual(['evil', 'evilness', 'bad', 'badness', 'bad', 'evil', 'ill'], antonyms)
