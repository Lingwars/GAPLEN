#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import product_reviews_1
camera_reviews = product_reviews_1.reviews('Canon_G3.txt')
review = camera_reviews[0]
print(review.sents()[0])
print(review.features())
print(product_reviews_1.features('Canon_G3.txt'))

n_reviews = len([(feat,score) for (feat,score) in product_reviews_1.features('Canon_G3.txt') if feat=='picture'])
tot = sum([int(score) for (feat,score) in product_reviews_1.features('Canon_G3.txt') if feat=='picture'])
# We use float for backward compatibility with division in Python2.7
mean = float(tot)/n_reviews
print(n_reviews, tot, mean)
