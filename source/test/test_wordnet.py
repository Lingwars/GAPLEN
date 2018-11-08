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
from nltk.corpus import wordnet

class TddInPythonExample(unittest.TestCase):

    def test_synonims_definition_method_returns_correct_result(self):
        syns = wordnet.synsets("program")
        s = syns[0].definition()
        self.assertEqual("a series of steps to be carried out or goals to be accomplished", s)

    def test_synonims_lemmas_method_returns_correct_result(self):
        syns = wordnet.synsets("program")
        s = syns[0].lemmas()[0].name()
        self.assertEqual("plan", s)

    def test_similarity_method_returns_correct_result(self):
        w1 = wordnet.synset('ship.n.01')
        w2 = wordnet.synset('boat.n.01')
        self.assertTrue(w1.wup_similarity(w2) > 0.5)

if __name__ == '__main__':
    unittest.main()
