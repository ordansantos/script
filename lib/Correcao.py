
import os
import filecmp
import os.path
import signal
import subprocess

import subprocess, threading
FNULL = open(os.devnull, 'w')

linguagens = ['cpp', 'py', 'java']

class Command(object):
	
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
            self.process = subprocess.Popen(self.cmd, shell=True, preexec_fn=os.setsid, stdout=FNULL, stderr=subprocess.STDOUT)
            self.process.communicate()

        thread = threading.Thread(target=target)
        thread.daemon = False
        thread.start()

        thread.join(timeout)
        
        if thread.is_alive():
            os.killpg(self.process.pid, signal.SIGTERM)
            thread.join()
            
        return self.process.returncode

def getLanguage (aluno, nome_problema):
	
	problema = 'alunos/' + aluno + '/' + nome_problema
	
	if os.path.isfile (problema + '.py'):
		return "py"
	if os.path.isfile (problema + '.java'):
		return "java"
	if os.path.isfile (problema + '.cpp'):
		return "cpp"
		
	for arquivo in os.listdir('alunos/' + aluno):
		if nome_problema in arquivo:
			return 'linguagem indefinida: ' + arquivo
		
	return 'arquivo inexistente'
	
def diff (file1, file2):
	txt1 = open (file1).read().strip();
	txt2 = open (file2).read().strip();
	return txt1 == txt2

def clear (problema):
	if os.path.isfile (problema):
		os.remove (problema)
		
	if os.path.isfile (problema + ".class"):
		os.remove (problema + ".class")
		
	if os.path.isfile ("out"):
		os.remove ("out")

def corrigir (problema, aluno):
	
	saida = "Problema: " + problema.getName() + '\n'
	
	lang = getLanguage(aluno, problema.getName())
	
	if lang not in linguagens:
		return (0, saida + lang)
	
	src = "alunos/" + aluno + "/" + problema.getName()
	compilation_code = 0
	
	if lang == 'cpp':
		compilation_code = subprocess.call(["g++", src + ".cpp", "-o", problema.getName()], stdout=FNULL, stderr=subprocess.STDOUT)
	
	if lang == 'java':
		compilation_code = subprocess.call(["javac", "-d", "./", src + ".java"], stdout=FNULL, stderr=subprocess.STDOUT)
	
	if compilation_code != 0:
		return (0, saida + "Erro de compilacao")
	
	pontos = 0		

	for i in range (problema.getNumberOfTests()):
		
		passou_teste = True
		tle = False
		runtime = False
		
		saida = saida + 'caso: ' + "%2d" % (i + 1) + ': '
		
		for caso in problema.getCasosDoTeste(i):
			
			command = ""
			
			if lang == 'cpp':	
				command = Command("./" + problema.getName() + " < " + caso[0] + " > out")
			
			if lang == 'py':
				command = Command("python " + src + ".py" + "< " + caso[0] + " > out")
			
			if lang == 'java':
				command = Command("java " + problema.getName() + " < " + caso[0] + " > out")
			
			code = command.run(timeout=3)

			if code == 0:
				if (diff(caso[1], 'out') == False): 
					passou_teste = False
					saida = saida + "X"
				else:
					saida = saida + "."
					
			if code == -15: 
				tle = True
				saida = saida + "T"
				
			if code == 139: 
				runtime = True
				saida = saida + "R"
				
			if code != 0 and code != -15 and code != 139: 
				passou_teste = False
				saida = saida + "?"
		
		
		if passou_teste and not tle and not runtime: 
			pontos += 1
		
		saida = saida + '\n'

	pontos = 1.0 * pontos / problema.getNumberOfTests() * 100
	saida = saida +  "Pontos: " + str(pontos)
	
	clear(problema.getName())
	
	return (pontos, saida)

