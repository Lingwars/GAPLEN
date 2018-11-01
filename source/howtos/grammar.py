#!/usr/bin/python
#-*- coding: utf-8 -*-

from nltk import CFG
grammar = CFG.fromstring("""
 S -> NP VP
 PP -> P NP
 NP -> Det N | NP PP
 VP -> V NP | VP PP
 Det -> 'a' | 'the'
 N -> 'dog' | 'cat'
 V -> 'chased' | 'sat'
 P -> 'on' | 'in'
 """)
print(grammar)
print(grammar.start())
print(grammar.productions()) # doctest: +NORMALIZE_WHITESPACE

from nltk import PCFG
toy_pcfg1 = PCFG.fromstring("""
 S -> NP VP [1.0]
 NP -> Det N [0.5] | NP PP [0.25] | 'John' [0.1] | 'I' [0.15]
 Det -> 'the' [0.8] | 'my' [0.2]
 N -> 'man' [0.5] | 'telescope' [0.5]
 VP -> VP PP [0.1] | V NP [0.7] | V [0.2]
 V -> 'ate' [0.35] | 'saw' [0.65]
 PP -> P NP [1.0]
 P -> 'with' [0.61] | 'under' [0.39]
 """)

g = CFG.fromstring("VP^<TOP> -> VBP NP^<VP-TOP>")
print(g.productions()[0].lhs())
