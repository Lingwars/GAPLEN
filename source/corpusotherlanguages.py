import nltk
from nltk.corpus import cess_esp
from nltk.corpus import floresta

print(nltk.corpus.cess_esp.words()
print(nltk.corpus.floresta.words())
print(nltk.corpus.indian.words('hindi.pos'))
print(nltk.corpus.udhr.fileids())
print(nltk.corpus.udhr.words('Javanese-Latin1')[11:])
