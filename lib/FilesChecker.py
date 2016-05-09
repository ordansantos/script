
import os

def check(problems, linguagens):
	
	for filename in os.listdir("alunos"):
		if " " in filename:
			raise Exception ('Nome de aluno com espaco: ' + filename)
		
	for aluno in os.listdir("alunos"):
		for filename in os.listdir("alunos/" + aluno):
			arquivo = os.path.splitext(filename)[0]
			extensao = os.path.splitext(filename)[1]
			
			if extensao not in linguagens:
				raise Exception ("Linguagem invalida do aluno " + aluno + ": " + filename)
			
			existeProblema = False
			for p in problems:
				if arquivo == p.getName():
					existeProblema = True
			
			if existeProblema == False:
				raise Exception ("Nome de problema invalido do aluno " + aluno + ": " + filename)
				
	
