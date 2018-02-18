#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk import *
from nltk.inference.nonmonotonic import *
from nltk.sem import logic
logic._counter._value = 0
read_expr = logic.Expression.fromstring

# Closed Domain Assumption

p1 = read_expr(r'all x.(man(x) -> mortal(x))')
p2 = read_expr(r'man(Socrates)')
c = read_expr(r'mortal(Socrates)')
prover = Prover9Command(c, [p1,p2])
prover.prove()
cdp = ClosedDomainProver(prover)
for a in cdp.assumptions():
    print(a) # doctest: +SKIP
cdp.prove()
p1 = read_expr(r'exists x.walk(x)')
p2 = read_expr(r'man(Socrates)')
c = read_expr(r'walk(Socrates)')
prover = Prover9Command(c, [p1,p2])
prover.prove()
cdp = ClosedDomainProver(prover)
for a in cdp.assumptions():
    print(a) # doctest: +SKIP
cdp.prove()
p1 = read_expr(r'exists x.walk(x)')
p2 = read_expr(r'man(Socrates)')
p3 = read_expr(r'-walk(Bill)')
c = read_expr(r'walk(Socrates)')
prover = Prover9Command(c, [p1,p2,p3])
prover.prove()
cdp = ClosedDomainProver(prover)
for a in cdp.assumptions():
    print(a) # doctest: +SKIP
cdp.prove()
p1 = read_expr(r'walk(Socrates)')
p2 = read_expr(r'walk(Bill)')
c = read_expr(r'all x.walk(x)')
prover = Prover9Command(c, [p1,p2])
prover.prove()
cdp = ClosedDomainProver(prover)
for a in cdp.assumptions():
    print(a) # doctest: +SKIP
print(cdp.goal()) # doctest: +SKIP
cdp.prove()
p1 = read_expr(r'girl(mary)')
p2 = read_expr(r'dog(rover)')
p3 = read_expr(r'all x.(girl(x) -> -dog(x))')
p4 = read_expr(r'all x.(dog(x) -> -girl(x))')
p5 = read_expr(r'chase(mary, rover)')
c = read_expr(r'exists y.(dog(y) & all x.(girl(x) -> chase(x,y)))')
prover = Prover9Command(c, [p1,p2,p3,p4,p5])
print(prover.prove())

cdp = ClosedDomainProver(prover)
for a in cdp.assumptions(): print(a) # doctest: +SKIP
print(cdp.goal()) # doctest: +SKIP
print(cdp.prove())

# Unique Names Assumption

p1 = read_expr(r'man(Socrates)')
p2 = read_expr(r'man(Bill)')
c = read_expr(r'exists x.exists y.-(x = y)')
prover = Prover9Command(c, [p1,p2])
prover.prove()
unp = UniqueNamesProver(prover)
for a in unp.assumptions(): print(a) # doctest: +SKIP
unp.prove()
p1 = read_expr(r'all x.(walk(x) -> (x = Socrates))')
p2 = read_expr(r'Bill = William')
p3 = read_expr(r'Bill = Billy')
c = read_expr(r'-walk(William)')
prover = Prover9Command(c, [p1,p2,p3])
prover.prove()

unp = UniqueNamesProver(prover)
for a in unp.assumptions(): print(a) # doctest: +SKIP
unp.prove()

# Closed World Assumption

p1 = read_expr(r'walk(Socrates)')
p2 = read_expr(r'-(Socrates = Bill)')
c = read_expr(r'-walk(Bill)')
prover = Prover9Command(c, [p1,p2])
prover.prove()
cwp = ClosedWorldProver(prover)
for a in cwp.assumptions(): print(a) # doctest: +SKIP
cwp.prove()
p1 = read_expr(r'see(Socrates, John)')
p2 = read_expr(r'see(John, Mary)')
p3 = read_expr(r'-(Socrates = John)')
p4 = read_expr(r'-(John = Mary)')
c = read_expr(r'-see(Socrates, Mary)')
prover = Prover9Command(c, [p1,p2,p3,p4])
prover.prove()
cwp = ClosedWorldProver(prover)
for a in cwp.assumptions(): print(a) # doctest: +SKIP
cwp.prove()
p1 = read_expr(r'all x.(ostrich(x) -> bird(x))')
p2 = read_expr(r'bird(Tweety)')
p3 = read_expr(r'-ostrich(Sam)')
p4 = read_expr(r'Sam != Tweety')
c = read_expr(r'-bird(Sam)')
prover = Prover9Command(c, [p1,p2,p3,p4])
prover.prove()
cwp = ClosedWorldProver(prover)
for a in cwp.assumptions(): print(a) # doctest: +SKIP
print(cwp.prove())

# Multi-Decorator Example

p1 = read_expr(r'see(Socrates, John)')
p2 = read_expr(r'see(John, Mary)')
c = read_expr(r'-see(Socrates, Mary)')
prover = Prover9Command(c, [p1,p2])
print(prover.prove())
cmd = ClosedDomainProver(UniqueNamesProver(ClosedWorldProver(prover)))
print(cmd.prove())

# Default Reasoning

logic._counter._value = 0
premises = []
premises.append(read_expr(r'all x.(elephant(x)        -> animal(x))'))
premises.append(read_expr(r'all x.(bird(x)            -> animal(x))'))
premises.append(read_expr(r'all x.(dove(x)            -> bird(x))'))
premises.append(read_expr(r'all x.(ostrich(x)         -> bird(x))'))
premises.append(read_expr(r'all x.(flying_ostrich(x)  -> ostrich(x))'))
premises.append(read_expr(r'all x.((animal(x)  & -Ab1(x)) -> -fly(x))')) #normal animals don't fly
premises.append(read_expr(r'all x.((bird(x)    & -Ab2(x)) -> fly(x))'))  #normal birds fly
premises.append(read_expr(r'all x.((ostrich(x) & -Ab3(x)) -> -fly(x))')) #normal ostriches don't fly
premises.append(read_expr(r'all x.(bird(x)           -> Ab1(x))')) #flight
premises.append(read_expr(r'all x.(ostrich(x)        -> Ab2(x))')) #non-flying bird
premises.append(read_expr(r'all x.(flying_ostrich(x) -> Ab3(x))')) #flying ostrich
premises.append(read_expr(r'elephant(el)'))
premises.append(read_expr(r'dove(do)'))
premises.append(read_expr(r'ostrich(os)'))
prover = Prover9Command(None, premises)
command = UniqueNamesProver(ClosedWorldProver(prover))
for a in command.assumptions(): print(a) # doctest: +SKIP
UniqueNamesProver(ClosedWorldProver(Prover9Command(read_expr('-fly(el)'), premises))).prove()
UniqueNamesProver(ClosedWorldProver(Prover9Command(read_expr('fly(do)'), premises))).prove()
UniqueNamesProver(ClosedWorldProver(Prover9Command(read_expr('-fly(os)'), premises))).prove()
