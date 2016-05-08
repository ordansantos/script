# coding: utf-8


from lib import *
import os

problems = Problem.getProblems()
resumo = ""

for aluno in os.listdir("alunos"):
	print "Aluno: " + aluno
	resumo = resumo + aluno + ": "
	total = 0
	for problem in problems:
		c = Correcao.corrigir (problem, aluno)
		total += c[0]
		print c[1] + '\n'
	print "Total: " + str(total) + '\n'
	resumo = resumo + str(total) + "\n"
	print ''
	
print "\t\n"

print resumo	

