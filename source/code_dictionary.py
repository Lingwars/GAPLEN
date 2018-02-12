# Natural Language Toolkit: code_dictionary

from collections import defaultdict
counts = defaultdict(int)
from nltk.corpus import brown
for (word, tag) in brown.tagged_words(categories='news', tagset='universal'):
     counts[tag] += 1

print counts['NOUN']
print sorted(counts)

from operator import itemgetter
sorted(counts.items(), key=itemgetter(1), reverse=True)
[t for t, c in sorted(counts.items(), key=itemgetter(1), reverse=True)]


