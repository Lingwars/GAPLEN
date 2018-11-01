#!/usr/bin/python# -*- coding: utf-8 -*-
from nltk.sem.logic import *
read_expr = Expression.fromstring

print(read_expr(r'john'))
print(read_expr(r'x'))
print(read_expr(r'-man(x)'))
print(read_expr(r'--man(x)'))
print(read_expr(r'(man(x))'))
print(read_expr(r'((man(x)))'))
print(read_expr(r'man(x) <-> tall(x)'))
print(read_expr(r'(man(x) <-> tall(x))'))
print(read_expr(r'(man(x) & tall(x) & walks(x))'))
print(read_expr(r'(man(x) & tall(x) & walks(x))').first)
print(read_expr(r'man(x) | tall(x) & walks(x)'))
print(read_expr(r'((man(x) & tall(x)) | walks(x))'))
print(read_expr(r'man(x) & (tall(x) | walks(x))'))
print(read_expr(r'(man(x) & (tall(x) | walks(x)))'))
print(read_expr(r'P(x) -> Q(x) <-> R(x) | S(x) & T(x)'))
print(read_expr(r'exists x.man(x)'))
print(read_expr(r'exists x.(man(x) & tall(x))'))
print(read_expr(r'exists x.(man(x) & tall(x) & walks(x))'))
print(read_expr(r'-P(x) & Q(x)'))
print(read_expr(r'-P(x) & Q(x)') == read_expr(r'(-P(x)) & Q(x)'))
print(read_expr(r'\x.man(x)'))
print(read_expr(r'\x.man(x)(john)'))
print(read_expr(r'\x.man(x)(john) & tall(x)'))
print(read_expr(r'\x.\y.sees(x,y)'))
print(read_expr(r'\x  y.sees(x,y)'))
print(read_expr(r'\x.\y.sees(x,y)(a)'))
print(read_expr(r'\x  y.sees(x,y)(a)'))
print(read_expr(r'\x.\y.sees(x,y)(a)(b)'))
print(read_expr(r'\x  y.sees(x,y)(a)(b)'))
print(read_expr(r'\x.\y.sees(x,y)(a,b)'))
print(read_expr(r'\x  y.sees(x,y)(a,b)'))
print(read_expr(r'((\x.\y.sees(x,y))(a))(b)'))
print(read_expr(r'P(x)(y)(z)'))
print(read_expr(r'P(Q)'))
print(read_expr(r'P(Q(x))'))
print(read_expr(r'(\x.exists y.walks(x,y))(x)'))
print(read_expr(r'exists x.(x = john)'))
print(read_expr(r'((\P.\Q.exists x.(P(x) & Q(x)))(\x.dog(x)))(\x.bark(x))'))
a = read_expr(r'exists c.exists b.A(b,c) & A(b,c)')
b = read_expr(r'(exists c.(exists b.A(b,c))) & A(b,c)')
print(a == b)
a = read_expr(r'exists c.(exists b.A(b,c) & A(b,c))')
b = read_expr(r'exists c.((exists b.A(b,c)) & A(b,c))')
print(a == b)
print(read_expr(r'exists x.x = y'))
print(read_expr('A(B)(C)'))
print(read_expr('(A(B))(C)'))
print(read_expr('A((B)(C))'))
print(read_expr('A(B(C))'))
print(read_expr('(A)(B(C))'))
print(read_expr('(((A)))(((B))(((C))))'))
print(read_expr(r'A != B'))
print(read_expr('P(x) & x=y & P(y)'))

try:
    print(read_expr(r'\walk.walk(x)'))
except LogicalExpressionException as e:
    print(e)

try:
    print(read_expr(r'all walk.walk(john)'))
except LogicalExpressionException as e:
    print(e)

try:
    print(read_expr(r'x(john)'))
except LogicalExpressionException as e:
    print(e)

from nltk.sem.logic import LogicParser # hack to give access to custom quote chars
lpq = LogicParser()
lpq.quote_chars = [("'", "'", "\\", False)]
print(lpq.parse(r"(man(x) & 'tall\'s,' (x) & walks (x) )"))
lpq.quote_chars = [("'", "'", "\\", True)]
print(lpq.parse(r"'tall\'s,'"))
print(lpq.parse(r"'spaced name(x)'"))
print(lpq.parse(r"-'tall\'s,'(x)"))
print(lpq.parse(r"(man(x) & 'tall\'s,' (x) & walks (x) )"))
