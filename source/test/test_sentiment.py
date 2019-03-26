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
class TddInPythonExample(unittest.TestCase):

    def test_sentiment_variable_create_returns_correct_result(self):
        pos_tweets = [('I love this car', 'positive'),
                      ('This view is amazing', 'positive'),
                      ('I feel great this morning', 'positive'),
                      ('I am so excited about the concert', 'positive'),
                      ('He is my best friend', 'positive'),
                      ('This movie was great', 'positive'),
                      ('This movie was not pathetic', 'positive')]

        neg_tweets = [('I do not like this car', 'negative'),
                      ('This view is horrible', 'negative'),
                      ('I feel tired this morning', 'negative'),
                      ('I am not looking forward to the concert', 'negative'),
                      ('He is my enemy', 'negative'),
                      ('This is a pathetic movie', 'negative')]

        tweets_with_sentiment = []
        for (tweet, sentiment) in pos_tweets + neg_tweets:
            filtered_tweet_words = [word.lower() for word in tweet.split() if len(word) >= 3]
            tweets_with_sentiment.append((filtered_tweet_words, sentiment))

        self.assertEqual([(['love', 'this', 'car'], 'positive'), (['this', 'view', 'amazing'], 'positive'), (['feel', 'great', 'this', 'morning'], 'positive'), (['excited', 'about', 'the', 'concert'], 'positive'), (['best', 'friend'], 'positive'), (['this', 'movie', 'was', 'great'], 'positive'), (['this', 'movie', 'was', 'not', 'pathetic'], 'positive'), (['not', 'like', 'this', 'car'], 'negative'), (['this', 'view', 'horrible'], 'negative'), (['feel', 'tired', 'this', 'morning'], 'negative'), (['not', 'looking', 'forward', 'the', 'concert'], 'negative'), (['enemy'], 'negative'), (['this', 'pathetic', 'movie'], 'negative')], tweets_with_sentiment)
