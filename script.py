# coding: utf-8


from lib import *

p = Problem.getProblems()[1]

c = Correcao.corrigir (p, "ordan")
print c[0]
print c[1] 
