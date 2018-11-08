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
from nltk.classify import SklearnClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC
class TddInPythonExample(unittest.TestCase):

    def test_svc_returns_correct_result(self):
        train_data = [({"a": 4, "b": 1, "c": 0}, "ham"),
                      ({"a": 5, "b": 2, "c": 1}, "ham"),
                      ({"a": 0, "b": 3, "c": 4}, "spam"),
                      ({"a": 5, "b": 1, "c": 1}, "ham"),
                      ({"a": 1, "b": 4, "c": 3}, "spam")]
        classif = SklearnClassifier(SVC(), sparse=False).train(train_data)
        test_data = [{"a": 3, "b": 2, "c": 1},
                     {"a": 0, "b": 3, "c": 7}]
        ccm =  classif.classify_many(test_data)
        self.assertEqual(ccm, ['ham', 'spam'])

#print(classifier.classify_many(test))
