import nltk

print(nltk.corpus.abc.words())
print(nltk.corpus.genesis.words())
print(nltk.corpus.gutenberg.words(fileids='austen-emma.txt'))
print(nltk.corpus.inaugural.words())
print(nltk.corpus.state_union.words())
print(nltk.corpus.webtext.words())
