#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.sem.logic import *
read_expr = Expression.fromstring

examples = [r'walk(john)',
            r'walk(x)',
            r'?vp(?np)',
            r'see(john,mary)',
            r'exists x.walk(x)',
            r'\x.see(john,x)',
            r'\x.see(john,x)(mary)',
            r'P(x)',
            r'\P.P(x)',
            r'aa(x,bb(y),cc(z),P(w),u)',
            r'bo(?det(?n),@x)']

examples = [read_expr(e) for e in examples]

for e in examples:
    print('%-25s' % e, sorted(e.free()))

for e in examples:
    print('%-25s' % e, sorted(e.constants()))

for e in examples:
    print('%-25s' % e, sorted(e.predicates()))

for e in examples:
    print('%-25s' % e, sorted(e.variables()))

print(read_expr(r'\e083.(walk(e083, z472) & talk(e092, z938))').normalize())
