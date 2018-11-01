import nltk
from nltk.corpus import PlaintextCorpusReader

corpus_root = '/usr/share/dict'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
print(wordlists.fileids())
print(wordlists.words('cracklib-small'))
