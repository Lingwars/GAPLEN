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
from nltk.classify import maxent
class TddInPythonExample(unittest.TestCase):

    def test_maxent_returns_correct_result(self):
        train = [
            ({'a': 1, 'b': 1, 'c': 1}, 'y'),
            ({'a': 5, 'b': 5, 'c': 5}, 'x'),
            ({'a': 0.9, 'b': 0.9, 'c': 0.9}, 'y'),
            ({'a': 5.5, 'b': 5.4, 'c': 5.3}, 'x'),
            ({'a': 0.8, 'b': 1.2, 'c': 1}, 'y'),
            ({'a': 5.1, 'b': 4.9, 'c': 5.2}, 'x')
        ]
        test = [
            {'a': 1, 'b': 0.8, 'c': 1.2},
            {'a': 5.2, 'b': 5.1, 'c': 5}
        ]
        encoding = maxent.TypedMaxentFeatureEncoding.train(train, count_cutoff=3, alwayson_features=True)
        classifier = maxent.MaxentClassifier.train(train, bernoulli=False, encoding=encoding, trace=0)
        self.assertEqual(classifier.classify_many(test), ['y', 'x'])

#print(classifier.classify_many(test))
