#!/usr/bin/python
# -*- coding: utf-8 -*-

# NAMED ENTITIES

from nltk.corpus import ieer
docs = ieer.parsed_docs('NYT_19980315')
tree = docs[1].text
print(tree) # doctest: +ELLIPSIS

from nltk.corpus import conll2002
for doc in conll2002.chunked_sents('ned.train')[27]:
    print(doc)

from nltk.sem import relextract
pairs = relextract.tree2semi_rel(tree)
for s, tree in pairs[18:22]:
    print('("...%s", %s)' % (" ".join(s[-5:]),tree))

reldicts = relextract.semi_rel2reldict(pairs)
for k, v in sorted(reldicts[0].items()):
    print(k, '=>', v) # doctest: +ELLIPSIS

for r in reldicts[18:20]:
    print('=' * 20)
    print(r['subjtext'])
    print(r['filler'])
    print(r['objtext'])

import re
IN = re.compile(r'.*\bin\b(?!\b.+ing\b)')
for fileid in ieer.fileids():
    for doc in ieer.parsed_docs(fileid):
        for rel in relextract.extract_rels('ORG', 'LOC', doc, corpus='ieer', pattern = IN):
            print(relextract.rtuple(rel))  # doctest: +ELLIPSIS

roles = """
(.*(
analyst|
chair(wo)?man|
commissioner|
counsel|
director|
economist|
editor|
executive|
foreman|
governor|
head|
lawyer|
leader|
librarian).*)|
manager|
partner|
president|
producer|
professor|
researcher|
spokes(wo)?man|
writer|
,\sof\sthe?\s*  # "X, of (the) Y"
"""

ROLES = re.compile(roles, re.VERBOSE)
for fileid in ieer.fileids():
    for doc in ieer.parsed_docs(fileid):
        for rel in relextract.extract_rels('PER', 'ORG', doc, corpus='ieer', pattern=ROLES):
            print(relextract.rtuple(rel)) # doctest: +ELLIPSS


de = """
.*
(
de/SP|
del/SP
)
"""

DE = re.compile(de, re.VERBOSE)
rels = [rel for doc in conll2002.chunked_sents('esp.train')
        for rel in relextract.extract_rels('ORG', 'LOC', doc, corpus='conll2002', pattern = DE)]
for r in rels[:10]:
    print(relextract.clause(r, relsym='DE'))    # doctest: +NORMALIZE_WHITESPACE

vnv = """
(
is/V|
was/V|
werd/V|
wordt/V
)
.*
van/Prep
"""

VAN = re.compile(vnv, re.VERBOSE)
for doc in conll2002.chunked_sents('ned.train'):
    for r in relextract.extract_rels('PER', 'ORG', doc, corpus='conll2002', pattern=VAN):
        print(relextract.clause(r, relsym="VAN"))


# RELATION EXTRACTION

# from nltk.sem import relextract
# pairs = relextract.tree2semi_rel(tree)
# for s, tree in pairs[18:22]:
#     print('("...%s", %s)' % (" ".join(s[-5:]), tree))

# reldicts = relextract.semi_rel2reldict(pairs)
# for k, v in sorted(reldicts[0].items()):
#     print(k, '=>', v) # doctest: +ELLIPSIS

# for r in reldicts[18:20]:
#     print('=' * 20)
#     print(r['subjtext'])
#     print(r['filler'])
#     print(r['objtext'])

    
# import re
# IN = re.compile(r'.*\bin\b(?!\b.+ing\b)')
# for fileid in ieer.fileids():
#     for doc in ieer.parsed_docs(fileid):
#         for rel in relextract.extract_rels('ORG', 'LOC', doc, corpus='ieer', pattern = IN):
#             print(relextract.rtuple(rel))  # doctest: +ELLIPSIS

# roles = """
# (.*(
# analyst|
# chair(wo)?man|
# commissioner|
# counsel|
# director|
# economist|
# editor|
# executive|
# foreman|
# governor|
# head|
# lawyer|
# leader|
# librarian).*)|
# manager|
# partner|
# president|
# producer|
# professor|
# researcher|
# spokes(wo)?man|
# writer|
# ,\sof\sthe?\s*  # "X, of (the) Y"
# """
# ROLES = re.compile(roles, re.VERBOSE)
# for fileid in ieer.fileids():
#     for doc in ieer.parsed_docs(fileid):
#         for rel in relextract.extract_rels('PER', 'ORG', doc, corpus='ieer', pattern=ROLES):
#             print(relextract.rtuple(rel)) # doctest: +ELLIPSIS            
