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

import nltk
nltk.usage(nltk.classify.ClassifierI)
from pprint import pprint

train = [
     (dict(a=1,b=1,c=1), 'y'),
     (dict(a=1,b=1,c=1), 'x'),
     (dict(a=1,b=1,c=0), 'y'),
     (dict(a=0,b=1,c=1), 'x'),
     (dict(a=0,b=1,c=1), 'y'),
     (dict(a=0,b=0,c=1), 'y'),
     (dict(a=0,b=1,c=0), 'x'),
     (dict(a=0,b=0,c=0), 'x'),
     (dict(a=0,b=1,c=1), 'y'),
     ]
test = [
     (dict(a=1,b=0,c=1)), # unseen
     (dict(a=1,b=0,c=0)), # unseen
     (dict(a=0,b=1,c=1)), # seen 3 times, labels=y,y,x
     (dict(a=0,b=1,c=0)), # seen 1 time, label=x
     ]

classifier = nltk.classify.NaiveBayesClassifier.train(train)
sorted(classifier.labels())
classifier.classify_many(test)
for pdist in classifier.prob_classify_many(test):
     print('%.4f %.4f' % (pdist.prob('x'), pdist.prob('y')))

classifier.show_most_informative_features()

classifier = nltk.classify.DecisionTreeClassifier.train(train, entropy_cutoff=0, support_cutoff=0)
sorted(classifier.labels())
print(classifier)
classifier.classify_many(test)
# for pdist in classifier.prob_classify_many(test):
#      print('%.4f %.4f' % (pdist.prob('x'), pdist.prob('y')))

from nltk.classify import SklearnClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC
train_data = [({"a": 4, "b": 1, "c": 0}, "ham"),
               ({"a": 5, "b": 2, "c": 1}, "ham"),
               ({"a": 0, "b": 3, "c": 4}, "spam"),
               ({"a": 5, "b": 1, "c": 1}, "ham"),
               ({"a": 1, "b": 4, "c": 3}, "spam")]
classif = SklearnClassifier(BernoulliNB()).train(train_data)
test_data = [{"a": 3, "b": 2, "c": 1},
              {"a": 0, "b": 3, "c": 7}]
classif.classify_many(test_data)
classif = SklearnClassifier(SVC(), sparse=False).train(train_data)
classif.classify_many(test_data)

def print_maxent_test_header():
    print(' '*11+''.join(['      test[%s]  ' % i
                           for i in range(len(test))]))
    print(' '*11+'     p(x)  p(y)'*len(test))
    print('-'*(11+15*len(test)))

def test_maxent(algorithm):
    print('%11s' % algorithm)
    try:
        classifier = nltk.classify.MaxentClassifier.train(train, algorithm, trace=0, max_iter=1000)
    except Exception as e:
        print('Error: %r' % e)
        return

    for featureset in test:
        pdist = classifier.prob_classify(featureset)
        print('%8.2f%6.2f' % (pdist.prob('x'), pdist.prob('y')), end=' ')
        print()
print_maxent_test_header();
test_maxent('GIS');
test_maxent('IIS')
test_maxent('MEGAM');
test_maxent('TADM') # doctest: +SKIP


from nltk.classify import maxent
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
print(encoding)
classifier = maxent.MaxentClassifier.train(train, bernoulli=False, encoding=encoding, trace=0)
print(classifier.classify_many(test))
