#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import twitter_samples
print(twitter_samples.fileids())
print(twitter_samples.strings('tweets.20150430-223406.json'))
print(twitter_samples.tokenized('tweets.20150430-223406.json'))
