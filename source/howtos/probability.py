import nltk
from nltk.probability import *

# FreqDist

text1 = ['no', 'good', 'fish', 'goes', 'anywhere', 'without', 'a', 'porpoise', '!']
text2 = ['no', 'good', 'porpoise', 'likes', 'to', 'fish', 'fish', 'anywhere', '.']
fd1 = nltk.FreqDist(text1)
fd1 == nltk.FreqDist(text1)

import itertools
both = nltk.FreqDist(text1 + text2)
both_most_common = both.most_common()
list(itertools.chain(*(sorted(ys) for k, ys in itertools.groupby(both_most_common, key=lambda t: t[1]))))
both == fd1 + nltk.FreqDist(text2)
fd1 == nltk.FreqDist(text1) # But fd1 is unchanged
fd2 = nltk.FreqDist(text2)
fd1.update(fd2)
fd1 == both
fd1 = nltk.FreqDist(text1)
fd1.update(text2)
fd1 == both
fd1 = nltk.FreqDist(text1)
fd2 = nltk.FreqDist(fd1)
print(fd2 == fd1)
import pickle
fd1 = nltk.FreqDist(text1)
pickled = pickle.dumps(fd1)
fd1 == pickle.loads(pickled)
print(fd1)

# Testing some HMM estimators

corpus = nltk.corpus.brown.tagged_sents(categories='adventure')[:500]
print(len(corpus))
from nltk.util import unique_list
tag_set = unique_list(tag for sent in corpus for (word,tag) in sent)
print(len(tag_set))
symbols = unique_list(word for sent in corpus for (word,tag) in sent)
print(len(symbols))
print(len(tag_set))
symbols = unique_list(word for sent in corpus for (word,tag) in sent)
print(len(symbols))
trainer = nltk.tag.HiddenMarkovModelTrainer(tag_set, symbols)
train_corpus = []
test_corpus = []
for i in range(len(corpus)):
    if i % 10:
        train_corpus += [corpus[i]]
    else:
        test_corpus += [corpus[i]]
print(len(train_corpus))
print(len(test_corpus))

def train_and_test(est):
    hmm = trainer.train_supervised(train_corpus, estimator=est)
    print('%.2f%%' % (100 * hmm.evaluate(test_corpus)))

# Maximum Likelihood Estimation

mle = lambda fd, bins: MLEProbDist(fd)
print(mle)

train_and_test(mle)
train_and_test(LaplaceProbDist)
train_and_test(ELEProbDist)

def lidstone(gamma):
    return lambda fd, bins: LidstoneProbDist(fd, gamma, bins)

train_and_test(lidstone(0.1))
train_and_test(lidstone(0.5))
train_and_test(lidstone(1.0))
