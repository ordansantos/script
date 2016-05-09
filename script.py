# coding: utf-8


from lib import *
import os

f = open ('resultados.txt', 'w')

problems = Problem.getProblems()
resumo = ""

for aluno in os.listdir("alunos"):
	
	print "Aluno: " + aluno
	f.write ("Aluno: " + aluno + '\n')
	
	resumo = resumo + aluno + ": "
	total = 0
	for problem in problems:
		c = Correcao.corrigir (problem, aluno)
		total += c[0]
		
		print c[1] + '\n'
		f.write (c[1] + '\n\n')
	
	print "Total: " + str(total) + '\n'
	f.write ("Total: " + str(total) + '\n\n')
	
	resumo = resumo + str(total) + "\n"
	
	print ''
	f.write ('\n')
	
print "\n"
f.write ('\n')

print resumo	
f.write (resumo)

f.close()

