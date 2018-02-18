#!/usr/bin/python# -*- coding: utf-8 -*-
from nltk.sem.logic import *
read_expr = Expression.fromstring

a = read_expr(r'a')
x = read_expr(r'x')
y = read_expr(r'y')
z = read_expr(r'z')
print(read_expr(r'man(x)').replace(x.variable, a, False))
print(read_expr(r'(man(x) & tall(x))').replace(x.variable, a, False))
print(read_expr(r'exists x.man(x)').replace(x.variable, a, False))
print(read_expr(r'exists x.man(x)').replace(x.variable, a, True))
print(read_expr(r'exists x.give(x,y,z)').replace(y.variable, a, False))
print(read_expr(r'exists x.give(x,y,z)').replace(y.variable, a, True))
e1 = read_expr(r'exists x.give(x,y,z)').replace(y.variable, x, False)
e2 = read_expr(r'exists z1.give(z1,x,z)')
e1 == e2
e1 = read_expr(r'exists x.give(x,y,z)').replace(y.variable, x, True)
e2 = read_expr(r'exists z1.give(z1,x,z)')
e1 == e2
print(read_expr(r'\x y z.give(x,y,z)').replace(y.variable, a, False))
print(read_expr(r'\x y z.give(x,y,z)').replace(y.variable, a, True))
print(read_expr(r'\x.\y.give(x,y,z)').replace(z.variable, a, False))
print(read_expr(r'\x.\y.give(x,y,z)').replace(z.variable, a, True))
e1 = read_expr(r'\x.\y.give(x,y,z)').replace(z.variable, x, False)
e2 = read_expr(r'\z1.\y.give(z1,y,x)')
e1 == e2
e1 = read_expr(r'\x.\y.give(x,y,z)').replace(z.variable, x, True)
e2 = read_expr(r'\z1.\y.give(z1,y,x)')
e1 == e2
print(read_expr(r'\x.give(x,y,z)').replace(z.variable, y, False))
print(read_expr(r'\x.give(x,y,z)').replace(z.variable, y, True))
from nltk.sem import logic
logic._counter._value = 0
e1 = read_expr('e1')
e2 = read_expr('e2')
print(read_expr('exists e1 e2.(walk(e1) & talk(e2))').replace(e1.variable, e2, True))

