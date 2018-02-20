#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import brown
suffix_fdist = nltk.FreqDist()
for word in brown.words():
     word = word.lower()
     suffix_fdist[word[-1:]] += 1
     suffix_fdist[word[-2:]] += 1
     suffix_fdist[word[-3:]] += 1
 	
common_suffixes = [suffix for (suffix, count) in suffix_fdist.most_common(100)]
print(common_suffixes)

def pos_features(sentence, i): 
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:]}
    if i == 0:
        features["prev-word"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
    return features  	

pos_features(brown.sents()[0], 8)

tagged_sents = brown.tagged_sents(categories='news')
featuresets = []
for tagged_sent in tagged_sents:
     untagged_sent = nltk.tag.untag(tagged_sent)
     for i, (word, tag) in enumerate(tagged_sent):
         featuresets.append( (pos_features(untagged_sent, i), tag) )

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set))
