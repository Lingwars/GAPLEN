# First, you're going to need to import wordnet:
from nltk.corpus import wordnet
 
# Then, we're going to use the term "program" to find synsets like so:
syns = wordnet.synsets("program")
 
# An example of a synset:
print(syns[0].name())
 
# Just the word:
print(syns[0].lemmas()[0].name())
 
# Definition of that first synset:
print(syns[0].definition())
 
# Examples of the word in use in sentences:
print(syns[0].examples())
