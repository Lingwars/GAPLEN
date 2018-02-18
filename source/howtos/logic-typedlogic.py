#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.sem.logic import LogicParser
tlp = LogicParser(True)
print(tlp.parse(r'man(x)').type)
print(tlp.parse(r'walk(angus)').type)
print(tlp.parse(r'-man(x)').type)
print(tlp.parse(r'(man(x) <-> tall(x))').type)
print(tlp.parse(r'exists x.(man(x) & tall(x))').type)
print(tlp.parse(r'\x.man(x)').type)
print(tlp.parse(r'john').type)
print(tlp.parse(r'\x y.sees(x,y)').type)
print(tlp.parse(r'\x.man(x)(john)').type)
print(tlp.parse(r'\x.\y.sees(x,y)(john)').type)
print(tlp.parse(r'\x.\y.sees(x,y)(john)(mary)').type)
print(tlp.parse(r'\P.\Q.exists x.(P(x) & Q(x))').type)
print(tlp.parse(r'\x.y').type)
print(tlp.parse(r'\P.P(x)').type)
parsed = tlp.parse('see(john,mary)')
print(parsed.type)
print(parsed.function)
print(parsed.function.type)
print(parsed.function.function)
print(parsed.function.function.type)
parsed = tlp.parse('P(x,y)')
print(parsed)
print(parsed.type)
print(parsed.function)
print(parsed.function.type)
print(parsed.function.function)
print(parsed.function.function.type)
print(tlp.parse(r'P').type)
print(tlp.parse(r'P', {'P': 't'}).type)
a = tlp.parse(r'P(x)')
print(a.type)
print(a.function.type)
print(a.argument.type)
a = tlp.parse(r'-P(x)')
print(a.type)
print(a.term.type)
print(a.term.function.type)
print(a.term.argument.type)
a = tlp.parse(r'P & Q')
print(a.type)
print(a.first.type)
print(a.second.type)
a = tlp.parse(r'(P(x) & Q(x))')
print(a.type)
print(a.first.type)
print(a.first.function.type)
print(a.first.argument.type)
print(a.second.type)
print(a.second.function.type)
print(a.second.argument.type)
a = tlp.parse(r'\x.P(x)')
print(a.type)
print(a.term.function.type)
print(a.term.argument.type)
a = tlp.parse(r'\P.P(x)')
print(a.type)
print(a.term.function.type)
print(a.term.argument.type)
a = tlp.parse(r'(\x.P(x)(john)) & Q(x)')
print(a.type)
print(a.first.type)
print(a.first.function.type)
print(a.first.function.term.function.type)
print(a.first.function.term.argument.type)
print(a.first.argument.type)
a = tlp.parse(r'\x y.P(x,y)(john)(mary) & Q(x)')
print(a.type)
print(a.first.type)
print(a.first.function.type)
print(a.first.function.function.type)
a = tlp.parse(r'--P')
print(a.type)
print(a.term.type)
print(a.term.term.type)
tlp.parse(r'\x y.P(x,y)').type
tlp.parse(r'\x y.P(x,y)', {'P': '<e,<e,t>>'}).type
a = tlp.parse(r'\P y.P(john,y)(\x y.see(x,y))')
a.type
a.function.type
a.function.term.term.function.function.type
a.argument.type
a = tlp.parse(r'exists c f.(father(c) = f)')
a.type
a.term.term.type
a.term.term.first.type
a.term.term.first.function.type
a.term.term.second.type

# typed check

a = tlp.parse('P(x)')
b = tlp.parse('Q(x)')
print(a.type)
c = a & b
c.first.type
c.typecheck() # doctest: +ELLIPSIS
c.first.type
a = tlp.parse('P(x)')
b = tlp.parse('P(x) & Q(x)')
#print(a.type)
#print(a.typecheck([a,b])) # doctest: +ELLIPSIS

e = tlp.parse(r'man(x)')
print(dict((k,str(v)) for k,v in e.typecheck().items()) == {'x': 'e', 'man': '<e,?>'})
sig = {'man': '<e, t>'}
e = tlp.parse(r'man(x)', sig)
print(e.function.type)
print(dict((k,str(v)) for k,v in e.typecheck().items()) == {'x': 'e', 'man': '<e,t>'})
print(e.function.type)
print(dict((k,str(v)) for k,v in e.typecheck(sig).items()) == {'x': 'e', 'man': '<e,t>'})


# findtype()

# print(tlp.parse(r'man(x)').findtype(Variable('man')))
# print(tlp.parse(r'see(x,y)').findtype(Variable('see')))
# print(tlp.parse(r'P(Q(R(x)))').findtype(Variable('Q')))

# reading types from strings

# Type.fromstring('e')
# Type.fromstring('<e,t>')
# Type.fromstring('<<e,t>,<e,t>>')
# Type.fromstring('<<e,?>,?>')

# # alternative type format

# Type.fromstring('e').str()
# Type.fromstring('<e,?>').str()
# Type.fromstring('<<e,t>,t>').str()

# Type.__eq__()

from nltk.sem.logic import *
e = ENTITY_TYPE
t = TRUTH_TYPE
a = ANY_TYPE
et = ComplexType(e,t)
eet = ComplexType(e,ComplexType(e,t))
at = ComplexType(a,t)
ea = ComplexType(e,a)
aa = ComplexType(a,a)
e == e
t == t
e == t
a == t
t == a
a == a
et == et
a == et
et == a
a == ComplexType(a,aa)
ComplexType(a,aa) == a

# matches()

e.matches(t)
a.matches(t)
t.matches(a)
a.matches(et)
et.matches(a)
ea.matches(eet)
eet.matches(ea)
aa.matches(et)
aa.matches(t)

# Type error during parsing

try:
    print(tlp.parse(r'exists x y.(P(x) & P(x,y))'))
except InconsistentTypeHierarchyException as e:
    print(e)

try:
    tlp.parse(r'\x y.see(x,y)(\x.man(x))')
except TypeException as e:
    print(e)

try:
    tlp.parse(r'\P x y.-P(x,y)(\x.-man(x))')
except TypeException as e:
    print(e)

a = tlp.parse(r'-talk(x)')
signature = a.typecheck()
try:
    print(tlp.parse(r'-talk(x,y)', signature))
except InconsistentTypeHierarchyException as e:
    print(e)

a = tlp.parse(r'-P(x)')
b = tlp.parse(r'-P(x,y)')
a.typecheck() # doctest: +ELLIPSIS
b.typecheck() # doctest: +ELLIPSIS

try:
    typecheck([a,b])
except InconsistentTypeHierarchyException as e:
    print(e)

a = tlp.parse(r'P(x)')
b = tlp.parse(r'P(x,y)')
signature = {'P': '<e,t>'}
a.typecheck(signature) # doctest: +ELLIPSIS

try:
    typecheck([a,b], signature)
except InconsistentTypeHierarchyException as e:
    print(e)
