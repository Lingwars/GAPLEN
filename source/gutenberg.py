import nltk
from nltk.corpus import gutenberg
print(nltk.corpus.gutenberg.fileids())
print(gutenberg.fileids())
print(gutenberg.words('austen-sense.txt'))

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)
