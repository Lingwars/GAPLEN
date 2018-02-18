#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import pros_cons
print(pros_cons.sents(categories='Cons'))
print(pros_cons.words('IntegratedPros.txt'))
