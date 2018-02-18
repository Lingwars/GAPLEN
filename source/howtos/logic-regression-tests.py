#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.sem.logic import *

read_expr = Expression.fromstring

e1 = read_expr('exists x.P(x)')
print(e1)
e2 = e1.alpha_convert(Variable('z'))
print(e2)
e1 == e2
l = read_expr(r'\X.\X.X(X)(1)').simplify()
id = read_expr(r'\X.X(X)')
l == id

zero = read_expr(r'\F x.x')
one = read_expr(r'\F x.F(x)')
two = read_expr(r'\F x.F(F(x))')
three = read_expr(r'\F x.F(F(F(x)))')
four = read_expr(r'\F x.F(F(F(F(x))))')
succ = read_expr(r'\N F x.F(N(F,x))')
plus = read_expr(r'\M N F x.M(F,N(F,x))')
mult = read_expr(r'\M N F.M(N(F))')
pred = read_expr(r'\N F x.(N(\G H.H(G(F)))(\u.x)(\u.u))')
v1 = ApplicationExpression(succ, zero).simplify()
v1 == one
v2 = ApplicationExpression(succ, v1).simplify()
v2 == two
v3 = ApplicationExpression(ApplicationExpression(plus, v1), v2).simplify()
v3 == three
v4 = ApplicationExpression(ApplicationExpression(mult, v2), v2).simplify()
v4 == four
v5 = ApplicationExpression(pred, ApplicationExpression(pred, v4)).simplify()
v5 == two

print(succ(zero).simplify() == one)
print(plus(one,two).simplify() == three)
print(mult(two,two).simplify() == four)
print(pred(pred(four)).simplify() == two)
john = read_expr(r'john')
man = read_expr(r'\x.man(x)')
walk = read_expr(r'\x.walk(x)')
man(john).simplify()
print(-walk(john).simplify())
print((man(john) & walk(john)).simplify())
print((man(john) | walk(john)).simplify())
print((man(john) > walk(john)).simplify())
print((man(john) < walk(john)).simplify())

john = VariableExpression(Variable('john'))
run_var = VariableExpression(Variable('run'))
run = lambda x: run_var(x)
run(john)

x1 = read_expr(r'\P.P(mia)(\x.walk(x))').simplify()
x2 = read_expr(r'walk(mia)').simplify()
x1 == x2
x1 = read_expr(r'exists x.(man(x) & ((\P.exists x.(woman(x) & P(x)))(\y.love(x,y))))').simplify()
x2 = read_expr(r'exists x.(man(x) & exists y.(woman(y) & love(x,y)))').simplify()
x1 == x2
x1 = read_expr(r'\a.sleep(a)(mia)').simplify()
x2 = read_expr(r'sleep(mia)').simplify()
x1 == x2
x1 = read_expr(r'\a.\b.like(b,a)(mia)').simplify()
x2 = read_expr(r'\b.like(b,mia)').simplify()
x1 == x2
x1 = read_expr(r'\a.(\b.like(b,a)(vincent))').simplify()
x2 = read_expr(r'\a.like(vincent,a)').simplify()
x1 == x2
x1 = read_expr(r'\a.((\b.like(b,a)(vincent)) & sleep(a))').simplify()
x2 = read_expr(r'\a.(like(vincent,a) & sleep(a))').simplify()
x1 == x2
x1 = read_expr(r'(\a.\b.like(b,a)(mia)(vincent))').simplify()
x2 = read_expr(r'like(vincent,mia)').simplify()
x1 == x2
x1 = read_expr(r'P((\a.sleep(a)(vincent)))').simplify()
x2 = read_expr(r'P(sleep(vincent))').simplify()
x1 == x2
x1 = read_expr(r'\A.A((\b.sleep(b)(vincent)))').simplify()
x2 = read_expr(r'\A.A(sleep(vincent))').simplify()
x1 == x2
x1 = read_expr(r'\A.A(sleep(vincent))').simplify()
x2 = read_expr(r'\A.A(sleep(vincent))').simplify()
x1 == x2
x1 = read_expr(r'(\A.A(vincent)(\b.sleep(b)))').simplify()
x2 = read_expr(r'sleep(vincent)').simplify()
x1 == x2
x1 = read_expr(r'\A.believe(mia,A(vincent))(\b.sleep(b))').simplify()
x2 = read_expr(r'believe(mia,sleep(vincent))').simplify()
x1 == x2
x1 = read_expr(r'(\A.(A(vincent) & A(mia)))(\b.sleep(b))').simplify()
x2 = read_expr(r'(sleep(vincent) & sleep(mia))').simplify()
x1 == x2
x1 = read_expr(r'\A.\B.(\C.C(A(vincent))(\d.probably(d)) & (\C.C(B(mia))(\d.improbably(d))))(\f.walk(f))(\f.talk(f))').simplify()
x2 = read_expr(r'(probably(walk(vincent)) & improbably(talk(mia)))').simplify()
x1 == x2
x1 = read_expr(r'(\a.\b.(\C.C(a,b)(\d.\f.love(d,f))))(jules)(mia)').simplify()
x2 = read_expr(r'love(jules,mia)').simplify()
x1 == x2
x1 = read_expr(r'(\A.\B.exists c.(A(c) & B(c)))(\d.boxer(d),\d.sleep(d))').simplify()
x2 = read_expr(r'exists c.(boxer(c) & sleep(c))').simplify()
x1 == x2
x1 = read_expr(r'\A.Z(A)(\c.\a.like(a,c))').simplify()
x2 = read_expr(r'Z(\c.\a.like(a,c))').simplify()
x1 == x2
x1 = read_expr(r'\A.\b.A(b)(\c.\b.like(b,c))').simplify()
x2 = read_expr(r'\b.(\c.\b.like(b,c)(b))').simplify()
x1 == x2
x1 = read_expr(r'(\a.\b.(\C.C(a,b)(\b.\a.loves(b,a))))(jules)(mia)').simplify()
x2 = read_expr(r'loves(jules,mia)').simplify()
x1 == x2
x1 = read_expr(r'(\A.\b.(exists b.A(b) & A(b)))(\c.boxer(c))(vincent)').simplify()
x2 = read_expr(r'((exists b.boxer(b)) & boxer(vincent))').simplify()
x1 == x2

