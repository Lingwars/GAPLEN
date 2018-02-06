# Natural Language Toolkit: code_three_word_phrase
# Searching for Three-Word Phrases Using POS Tags
import nltk
from nltk.corpus import brown
def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence): # [_three-word]
        if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')): # [_verb-to-verb]
            print(w1, w2, w3) # [_print-words]

for tagged_sent in brown.tagged_sents():
    process(tagged_sent)
