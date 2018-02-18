#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import shakespeare
from xml.etree import ElementTree
shakespeare.fileids() # doctest: +ELLIPSIS
play = shakespeare.xml('dream.xml')
print(play) # doctest: +ELLIPSIS
print('%s: %s' % (play[0].tag, play[0].text))
personae = [persona.text for persona in
             play.findall('PERSONAE/PERSONA')]
print(personae) # doctest: +ELLIPSIS
# Find and print speakers not listed as personae
names = [persona.split(',')[0] for persona in personae]
speakers = set(speaker.text for speaker in
                play.findall('*/*/*/SPEAKER'))
print(sorted(speakers.difference(names))) 
