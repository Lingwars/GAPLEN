#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk import *
from nltk.sem.drt import DrtParser
from nltk.sem import logic
logic._counter._value = 0

from nltk.sem import Expression
read_expr = Expression.fromstring
p1 = read_expr('man(socrates)')
p2 = read_expr('all x.(man(x) -> mortal(x))')
c  = read_expr('mortal(socrates)')
Prover9().prove(c, [p1,p2])
# TableauProver().prove(c, [p1,p2])
# ResolutionProver().prove(c, [p1,p2], verbose=True)

# THE PROVER COMMAND

# prover = ResolutionProverCommand(c, [p1,p2])
# print(prover.proof()) # doctest: +ELLIPSIS
# print(prover.prove())
# print(prover.proof())

# print(prover.prove())

# print(prover.assumptions())
# print(prover.goal())

# print(prover.retract_assumptions([read_expr('man(socrates)')]))
# print(prover.proof()) # doctest: +ELLIPSIS
# print(prover.prove())
# print(prover.proof())
# print(pprover.add_assumptions([read_expr('man(socrates)')]))
# print(prover.prove())

# PROVER9

