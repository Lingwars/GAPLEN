from nltk.sem import logic
from nltk.sem.glue import *
from nltk.sem.linearlogic import *
from nltk.sem.linearlogic import Expression
read_expr = Expression.fromstring

# Parser
print(read_expr(r'f'))
print(read_expr(r'(g -o f)'))
print(read_expr(r'(g -o (h -o f))'))
print(read_expr(r'((g -o G) -o G)'))
print(read_expr(r'(g -o f)(g)'))
print(read_expr(r'((g -o G) -o G)((g -o f))'))

# Simplify
print(read_expr(r'f').simplify())
print(read_expr(r'(g -o f)').simplify())
print(read_expr(r'((g -o G) -o G)').simplify())
print(read_expr(r'(g -o f)(g)').simplify())
try:
    read_expr(r'(g -o f)(f)').simplify()
except LinearLogicApplicationException as e:
    print(e)

print(read_expr(r'(G -o f)(g)').simplify())
print(read_expr(r'((g -o G) -o G)((g -o f))').simplify())

# Test BindingDict
h = ConstantExpression('h')
g = ConstantExpression('g')
f = ConstantExpression('f')
H = VariableExpression('H')
G = VariableExpression('G')
F = VariableExpression('F')
d1 = BindingDict({H: h})
d2 = BindingDict({F: f, G: F})
d12 = d1 + d2
all12 = ['%s: %s' % (v, d12[v]) for v in d12.d]
all12.sort()
print(all12)
BindingDict([(F,f),(G,g),(H,h)]) == BindingDict({F:f, G:g, H:h})
d4 = BindingDict({F: f})
try:
    d4[F] = g
except VariableBindingException as e:
    print(e)

# Test Unify

try:
    f.unify(g, BindingDict())
except UnificationException as e:
    print(e)

f.unify(G, BindingDict()) == BindingDict({G: f})
try:
    f.unify(G, BindingDict({G: h}))
except UnificationException as e:
    print(e)

f.unify(G, BindingDict({G: f})) == BindingDict({G: f})
f.unify(G, BindingDict({H: f})) == BindingDict({G: f, H: f})
G.unify(f, BindingDict()) == BindingDict({G: f})
try:
    G.unify(f, BindingDict({G: h}))
except UnificationException as e:
    print(e)

G.unify(f, BindingDict({G: f})) == BindingDict({G: f})
G.unify(f, BindingDict({H: f})) == BindingDict({G: f, H: f})
G.unify(F, BindingDict()) == BindingDict({G: F})
try:
    G.unify(F, BindingDict({G: H}))
except UnificationException as e:
    print(e)

G.unify(F, BindingDict({G: F})) == BindingDict({G: F})
G.unify(F, BindingDict({H: F})) == BindingDict({G: F, H: F})

# Test Compile

print(read_expr('g').compile_pos(Counter(), GlueFormula))
print(read_expr('(g -o f)').compile_pos(Counter(), GlueFormula))
print(read_expr('(g -o (h -o f))').compile_pos(Counter(), GlueFormula))

# Demo of "John walks"

john = GlueFormula("John", "g")
print(john)
walks = GlueFormula(r"\x.walks(x)", "(g -o f)")
print(walks)
print(walks.applyto(john))
print(walks.applyto(john).simplify())

# Demo of "A dog walks"

a = GlueFormula("\P Q.some x.(P(x) and Q(x))", "((gv -o gr) -o ((g -o G) -o G))")
print(a)
man = GlueFormula(r"\x.man(x)", "(gv -o gr)")
print(man)
walks = GlueFormula(r"\x.walks(x)", "(g -o f)")
print(walks)
a_man = a.applyto(man)
print(a_man.simplify())
a_man_walks = a_man.applyto(walks)
print(a_man_walks.simplify())

############ Demo of 'every girl chases a dog'

# Individual words
every = GlueFormula("\P Q.all x.(P(x) -> Q(x))", "((gv -o gr) -o ((g -o G) -o G))")
print(every)
# \P Q.all x.(P(x) -> Q(x)) : ((gv -o gr) -o ((g -o G) -o G))
girl = GlueFormula(r"\x.girl(x)", "(gv -o gr)")
print(girl)
# \x.girl(x) : (gv -o gr)
chases = GlueFormula(r"\x y.chases(x,y)", "(g -o (h -o f))")
print(chases)
# \x y.chases(x,y) : (g -o (h -o f))
a = GlueFormula("\P Q.some x.(P(x) and Q(x))", "((hv -o hr) -o ((h -o H) -o H))")
print(a)
# \P Q.exists x.(P(x) & Q(x)) : ((hv -o hr) -o ((h -o H) -o H))
dog = GlueFormula(r"\x.dog(x)", "(hv -o hr)")
print(dog)


# Noun Quantification
every = GlueFormula("\P Q.all x.(P(x) -> Q(x))", "((gv -o gr) -o ((g -o G) -o G))")
print(every)
girl = GlueFormula(r"\x.girl(x)", "(gv -o gr)")
print(girl)
chases = GlueFormula(r"\x y.chases(x,y)", "(g -o (h -o f))")
print(chases)
a = GlueFormula("\P Q.some x.(P(x) and Q(x))", "((hv -o hr) -o ((h -o H) -o H))")
print(a)
dog = GlueFormula(r"\x.dog(x)", "(hv -o hr)")
print(dog)


every_girl = every.applyto(girl)
print(every_girl.simplify())
a_dog = a.applyto(dog)
print(a_dog.simplify())

xPrime = GlueFormula("x1", "g")
print(xPrime)
xPrime_chases = chases.applyto(xPrime)
print(xPrime_chases.simplify())
xPrime_chases_a_dog = a_dog.applyto(xPrime_chases)
print(xPrime_chases_a_dog.simplify())


chases_a_dog = xPrime_chases_a_dog.lambda_abstract(xPrime)
print(chases_a_dog.simplify())
every_girl_chases_a_dog = every_girl.applyto(chases_a_dog)
r1 = every_girl_chases_a_dog.simplify()
r2 = GlueFormula(r'all x.(girl(x) -> exists z1.(dog(z1) & chases(x,z1)))', 'f')
print(r1 == r2)


xPrime = GlueFormula("x1", "g")
print(xPrime)
xPrime_chases = chases.applyto(xPrime)
print(xPrime_chases.simplify())
yPrime = GlueFormula("x2", "h")
print(yPrime)
xPrime_chases_yPrime = xPrime_chases.applyto(yPrime)
print(xPrime_chases_yPrime.simplify())
chases_yPrime = xPrime_chases_yPrime.lambda_abstract(xPrime)
print(chases_yPrime.simplify())
every_girl_chases_yPrime = every_girl.applyto(chases_yPrime)
print(every_girl_chases_yPrime.simplify())
every_girl_chases = every_girl_chases_yPrime.lambda_abstract(yPrime)
print(every_girl_chases.simplify())
every_girl_chases_a_dog = a_dog.applyto(every_girl_chases)
r1 = every_girl_chases_a_dog.simplify()
r2 = GlueFormula(r'exists x.(dog(x) & all z2.(girl(z2) -> chases(z2,x)))', 'f')
print(r1 == r2)


# Compilation
for cp in GlueFormula('m', '(b -o a)').compile(Counter()): print(cp)
for cp in GlueFormula('m', '((c -o b) -o a)').compile(Counter()): print(cp)
for cp in GlueFormula('m', '((d -o (c -o b)) -o a)').compile(Counter()): print(cp)
for cp in GlueFormula('m', '((d -o e) -o ((c -o b) -o a))').compile(Counter()): print(cp)
for cp in GlueFormula('m', '(((d -o c) -o b) -o a)').compile(Counter()): print(cp)
for cp in GlueFormula('m', '((((e -o d) -o c) -o b) -o a)').compile(Counter()): print(cp)

# Demo of 'a man walks' using Compilation
a = GlueFormula('\\P Q.some x.(P(x) and Q(x))', '((gv -o gr) -o ((g -o G) -o G))')
print(a)
man = GlueFormula('\\x.man(x)', '(gv -o gr)')
print(man)
walks = GlueFormula('\\x.walks(x)', '(g -o f)')
print(walks)

# Compiled premises
counter = Counter()
ahc = a.compile(counter)
g1 = ahc[0]
print(g1)
g2 = ahc[1]
print(g2)
g3 = ahc[2]
print(g3)
g4 = man.compile(counter)[0]
print(g4)
g5 = walks.compile(counter)[0]
print(g5)

# Dependency Graph to Glue Formulas
from nltk.corpus.reader.dependency import DependencyGraph
depgraph = DependencyGraph("""1 John    _       NNP     NNP     _       2       SUBJ    _       _
 2       sees    _       VB      VB      _       0       ROOT    _       _
 3       a       _       ex_quant        ex_quant        _       4       SPEC    _       _
 4       dog     _       NN      NN      _       2       OBJ     _       _
 """)
gfl = GlueDict('nltk:grammars/sample_grammars/glue.semtype').to_glueformula_list(depgraph)
for gf in gfl:
    print(gf)
glue = Glue()
for r in sorted([r.simplify().normalize() for r in glue.get_readings(glue.gfl_to_compiled(gfl))], key=str):
    print(r)

# Dependency Graph to LFG f-structure

from nltk.sem.lfg import FStructure
fstruct = FStructure.read_depgraph(depgraph)
print(fstruct)
fstruct.to_depgraph().tree().pprint()

for gf in fstruct.to_glueformula_list(GlueDict('nltk:grammars/sample_grammars/glue.semtype')): # doctest: +SKIP
    print(gf)

    
