import nltk
from nltk.corpus import inaugural
print inaugural.fileids()
print [fileid[:4] for fileid in inaugural.fileids()]
