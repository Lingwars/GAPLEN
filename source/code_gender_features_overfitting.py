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

print gender_features('John') 

from nltk.corpus import names
labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                 [(name, 'female') for name in names.words('female.txt')])
import random
random.shuffle(labeled_names)

featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print("Neo is " + classifier.classify(gender_features('Neo')))
print("Trinity is " + classifier.classify(gender_features('Trinity')))
print("The classifier has an accuracy: " + nltk.classify.accuracy(classifier, test_set))
print("The most informative features are: " + classifier.show_most_informative_features(5))
