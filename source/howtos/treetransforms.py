from copy import deepcopy
from nltk.tree import *
from nltk.treetransforms import *
tree_string = "(TOP (S (S (VP (VBN Turned) (ADVP (RB loose)) (PP (IN in) (NP (NP (NNP Shane) (NNP Longman) (POS 's)) (NN trading) (NN room))))) (, ,) (NP (DT the) (NN yuppie) (NNS dealers)) (VP (AUX do) (NP (NP (RB little)) (ADJP (RB right)))) (. .)))"
tree = Tree.fromstring(tree_string)
print(tree)

collapsedTree = deepcopy(tree)
collapse_unary(collapsedTree)
print(collapsedTree)

collapsedTree2 = deepcopy(tree)
collapse_unary(collapsedTree2, collapsePOS=True, collapseRoot=True)
print(collapsedTree2)

cnfTree = deepcopy(collapsedTree)
chomsky_normal_form(cnfTree, factor='left')
print(cnfTree)

markovTree = deepcopy(collapsedTree)
chomsky_normal_form(markovTree, horzMarkov=2, vertMarkov=1)
print(markovTree)

un_chomsky_normal_form(markovTree)
tree == markovTree
