#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import conll2000, conll2002
print(conll2000.sents()) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
for tree in conll2000.chunked_sents()[:2]:
    print(tree) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
print(conll2002.sents()) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
for tree in conll2002.chunked_sents()[:2]:
    print(tree) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE


# SEMCOR
    
from nltk.corpus import semcor
print(semcor.words())
print(semcor.chunks())
print(semcor.sents()) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
print(semcor.chunk_sents()) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
list(map(str, semcor.tagged_chunks(tag='both')[:3]))
[[str(c) for c in s] for s in semcor.tagged_sents(tag='both')[:2]]    

# IEER

from nltk.corpus import ieer
ieer.fileids() # doctest: +NORMALIZE_WHITESPACE
docs = ieer.parsed_docs('APW_19980314')
print(docs[0])
print(docs[0].docno)
print(docs[0].doctype)
print(docs[0].date_time)
print(docs[0].headline)
print(docs[0].text) # doctest: +ELLIPSIS
