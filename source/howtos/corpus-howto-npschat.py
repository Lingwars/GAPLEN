#!/usr/bin/python
# -*- coding: utf-8 -*-
import nltk

print(nltk.corpus.nps_chat.words())
print(nltk.corpus.nps_chat.tagged_words())
print(nltk.corpus.nps_chat.tagged_posts()) # doctest: +NORMALIZE_WHITESPACE
print(nltk.corpus.nps_chat.xml_posts()) # doctest: +ELLIPSIS
posts = nltk.corpus.nps_chat.xml_posts()
sorted(nltk.FreqDist(p.attrib['class'] for p in posts).keys())
posts[0].text
tokens = posts[0].findall('terminals/t')
for t in tokens:
    print(t.attrib['pos'] + "/" + t.attrib['word']) 
