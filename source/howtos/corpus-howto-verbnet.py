#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import verbnet
verbnet.lemmas()[20:25]
verbnet.classids()[:5]
verbnet.classids('accept')
verbnet.vnclass('remove-10.1') # doctest: +ELLIPSIS
verbnet.vnclass('10.1') # doctest: +ELLIPSIS
vn_31_2 = verbnet.vnclass('admire-31.2')
for themrole in vn_31_2.findall('THEMROLES/THEMROLE'):
     print(themrole.attrib['type'])
     for selrestr in themrole.findall('SELRESTRS/SELRESTR'):
         print('[%(Value)s%(type)s]' % selrestr.attrib)
     print()

print(verbnet.pprint('57'))
     
