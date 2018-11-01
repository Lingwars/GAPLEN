#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import ppattach
print(ppattach.attachments('training')) # doctest: +NORMALIZE_WHITESPACE
inst = ppattach.attachments('training')[0]
print(inst.sent, inst.verb, inst.noun1, inst.prep, inst.noun2)
print(inst.attachment)
