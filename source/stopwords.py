import nltk
from nltk.corpus import stopwords

print stopwords.words('english')
print stopwords.words('spanish')

def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)


