#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: David Arroyo Menéndez. All rights reserved.
# Natural Language Toolkit: code_gender_features_overfitting

import nltk

def gender_features(name):
    features = {}
    features["first_letter"] = name[0].lower()
    features["last_letter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = name.lower().count(letter)
        features["has({})".format(letter)] = (letter in name.lower())
    return features

myfile = open("bottlemembers.org", "a+")

def add_member():
    member = raw_input("Write the bottle member name: ")
    myfile.write(member + "\n")

add = raw_input("Do you want add a bottle member (y/n): ")
if (add == "y"):
    while True:    
        add_member()    
        other = raw_input("Do you want to continue (y/n): ")
        if (other == "n"):
            myfile.close
            break
    
filepath="bottlemembers.org"
l = []
with open(filepath) as f:
    for line in enumerate(f):
        print("Line {}".format(line))
        l.append(format(line))

import random
nombre1 = random.choice(l)
nombre2 = random.choice(l)

print("nombre1 is {}", nombre1)
print("nombre2 is {}", nombre2)

#print gender_features('John') 

from nltk.corpus import names
labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                 [(name, 'female') for name in names.words('female.txt')])
import random
random.shuffle(labeled_names)

featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

if ((classifier.classify(gender_features(nombre1)) == 'male') and (classifier.classify(gender_features(nombre2)) == 'female')) or ((classifier.classify(gender_features(nombre1)) == 'female') and (classifier.classify(gender_features(nombre2)) == 'male')):
    print(nombre1 + " is " + classifier.classify(gender_features(nombre1)))
    print(nombre2 + " is " + classifier.classify(gender_features(nombre2)))
else:
    print("This software is doing a joke, you can run again")

print("The classifier has an accuracy: " + str(nltk.classify.accuracy(classifier, test_set)))
print("The most informative features are: " + str(classifier.show_most_informative_features(5)))
