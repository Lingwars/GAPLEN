#!/usr/bin/python# -*- coding: utf-8 -*-
from nltk.sem.logic import *
read_expr = Expression.fromstring

print(read_expr(r'\x.man(x)(john)').simplify())
print(read_expr(r'\x.((man(x)))(john)').simplify())
print(read_expr(r'\x.\y.sees(x,y)(john, mary)').simplify())
print(read_expr(r'\x  y.sees(x,y)(john, mary)').simplify())
print(read_expr(r'\x.\y.sees(x,y)(john)(mary)').simplify())
print(read_expr(r'\x  y.sees(x,y)(john)(mary)').simplify())
print(read_expr(r'\x.\y.sees(x,y)(john)').simplify())
print(read_expr(r'\x  y.sees(x,y)(john)').simplify())
print(read_expr(r'(\x.\y.sees(x,y)(john))(mary)').simplify())
print(read_expr(r'(\x  y.sees(x,y)(john))(mary)').simplify())
print(read_expr(r'exists x.(man(x) & (\x.exists y.walks(x,y))(x))').simplify())
e1 = read_expr(r'exists x.(man(x) & (\x.exists y.walks(x,y))(y))').simplify()
e2 = read_expr(r'exists x.(man(x) & exists z1.walks(y,z1))')
print(e1 == e2)
print(read_expr(r'(\P Q.exists x.(P(x) & Q(x)))(\x.dog(x))').simplify())
print(read_expr(r'((\P.\Q.exists x.(P(x) & Q(x)))(\x.dog(x)))(\x.bark(x))').simplify())
print(read_expr(r'\P.(P(x)(y))(\a b.Q(a,b))').simplify())
