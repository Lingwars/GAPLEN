import nltk
from nltk.book import *
fdist1 = FreqDist(text1)
print fdist1
print fdist1.most_common(50)
print fdist1['whale']
