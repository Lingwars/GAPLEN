from nltk.corpus import reuters
print(reuters.fileids())
print(reuters.categories())
print(reuters.categories('training/9865'))
print(reuters.categories(['training/9865', 'training/9880']))
print(reuters.fileids('barley'))
print(reuters.fileids(['barley', 'corn']))
print(reuters.words('training/9865')[:14])
print(reuters.words(['training/9865', 'training/9880']))
