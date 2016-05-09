
import os
import filecmp
import os.path
import signal
import subprocess

import subprocess, threading
FNULL = open(os.devnull, 'w')

linguagens = ['cpp', 'py', 'java', 'c', 'pas']

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
	if os.path.isfile (problema + '.c'):
		return "c"
	if os.path.isfile (problema + '.pas'):
		return "pas"
		
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
		compilation_code = subprocess.call(["g++", "-g", "-O2", "-std=gnu++11", "-static", src + ".cpp", "-o", problema.getName()], stdout=FNULL, stderr=subprocess.STDOUT)
	
	if lang == 'c':
		compilation_code = subprocess.call(["gcc", "-g", "-O2", "-std=gnu99", "-static", src + ".c", "-lm", "-o", problema.getName()], stdout=FNULL, stderr=subprocess.STDOUT)
	
	if lang == 'java':
		compilation_code = subprocess.call(["javac", "-d", "./", src + ".java"], stdout=FNULL, stderr=subprocess.STDOUT)
		
	if lang == 'pas':
		compilation_code = subprocess.call(["pc", src + ".pas"], stdout=FNULL, stderr=subprocess.STDOUT)
		if os.path.isfile (src):
			os.rename (src, "./" + problema.getName())
		if os.path.isfile (src + ".o"):
			os.remove (src + ".o")
		
	if compilation_code != 0:
		return (0, saida + "Erro de compilacao")
	
	pontos = 0		

	for i in range (problema.getNumberOfTests()):
		
		passou_teste = True
		
		saida = saida + 'caso: ' + "%2d" % (i + 1) + ': '
		
		for caso in problema.getCasosDoTeste(i):
			
			command = ""
			
			if lang == 'cpp' or lang == 'c' or lang == 'pas':	
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
					
			if code != 0: passou_teste = False
					
			if code == -15: saida = saida + "T"
				
			if code == 139 or code == 1: saida = saida + "R"
				
			if code != 0 and code != -15 and code != 139 and code != 1: saida = saida + "?"
				
		if passou_teste: pontos += 1
		
		saida = saida + '\n'

	pontos = 1.0 * pontos / problema.getNumberOfTests() * 100
	saida = saida +  "Pontos: " + str(pontos)
	
	clear(problema.getName())
	
	return (pontos, saida)

