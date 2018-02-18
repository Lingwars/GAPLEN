#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.sem import logic
from nltk.inference import TableauProver

# OVERVIEW

# A DRS can be created with the DRS() constructor. This takes two arguments: a list of discourse referents and list of conditions. .
from nltk.sem.drt import *
dexpr = DrtExpression.fromstring
man_x = dexpr('man(x)')
walk_x = dexpr('walk(x)')
x = dexpr('x')
print(DRS([x], [man_x, walk_x]))

# The parse() method can also be applied directly to DRS expressions, which allows them to be specified more easily.
drs1 = dexpr('([x],[man(x),walk(x)])')
print(drs1)

# DRSs can be merged using the + operator.
drs2 = dexpr('([y],[woman(y),stop(y)])')
drs3 = drs1 + drs2
print(drs3)
print(drs3.simplify())

# We can embed DRSs as components of an implies condition.
s = '([], [(%s -> %s)])' % (drs1, drs2)
print(dexpr(s))

# The fol() method converts DRSs into FOL formulae.
print(dexpr(r'([x],[man(x), walks(x)])').fol())
print(dexpr(r'([],[(([x],[man(x)]) -> ([],[walks(x)]))])').fol())

# In order to visualize a DRS, the pretty_format() method can be used.
print(drs3.pretty_format())

# PARSE TO SEMANTICS

# DRSs can be used for building compositional semantics in a feature based grammar. To specify that we want to use DRSs, the appropriate logic parser needs be passed as a parameter to load_earley()
from nltk.parse import load_parser
from nltk.sem.drt import DrtParser
parser = load_parser('grammars/book_grammars/drt.fcfg', trace=0, logic_parser=DrtParser())
for tree in parser.parse('a dog barks'.split()):
    print(tree.label()['SEM'].simplify())

# Alternatively, a FeatStructReader can be passed with the logic_parser set on it    
from nltk.featstruct import FeatStructReader
from nltk.grammar import FeatStructNonterminal
parser = load_parser('grammars/book_grammars/drt.fcfg', trace=0, fstruct_reader=FeatStructReader(fdict_class=FeatStructNonterminal, logic_parser=DrtParser()))
for tree in parser.parse('every girl chases a dog'.split()):
    print(tree.label()['SEM'].simplify().normalize())

