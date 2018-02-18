#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import semcor
semcor.words('brown2/tagfiles/br-n12.xml')  # doctest: +ELLIPSIS
sent = semcor.xml('brown2/tagfiles/br-n12.xml').findall('context/p/s')[0]
for wordform in sent.getchildren():
    print(wordform.text)
    for key in sorted(wordform.keys()):
        print(key + '=' + wordform.get(key))
