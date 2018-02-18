#!/usr/bin/python
# -*- coding: utf-8 -*-
# The RTE (Recognizing Textual Entailment) corpus was derived from the RTE1, RTE2 and RTE3 datasets (dev and test data), and consists of a list of XML-formatted 'text'/'hypothesis' pairs.

from nltk.corpus import rte
print(rte.fileids()) # doctest: +ELLIPSIS
rtepairs = rte.pairs(['rte2_test.xml', 'rte3_test.xml'])
print(rtepairs)  # doctest: +ELLIPSIS
rtepairs[5]
rtepairs[5].text # doctest: +NORMALIZE_WHITESPACE
rtepairs[5].hyp
rtepairs[5].value
xmltree = rte.xml('rte3_dev.xml')
xmltree # doctest: +SKIP
xmltree[7].findtext('t') # doctest: +NORMALIZE_WHITESPACE
