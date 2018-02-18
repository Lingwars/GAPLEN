#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import senseval
print(senseval.fileids())
print(senseval.instances('hard.pos'))

for inst in senseval.instances('interest.pos')[:10]:
    p = inst.position
    left = ' '.join(w for (w,t) in inst.context[p-2:p])
    word = ' '.join(w for (w,t) in inst.context[p:p+1])
    right = ' '.join(w for (w,t) in inst.context[p+1:p+3])
    senses = ' '.join(inst.senses)
    print('%20s |%10s | %-15s -> %s' % (left, word, right, senses))
