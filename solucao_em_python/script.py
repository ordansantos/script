
# Universidade Federal de Campina Grande
# Script_CPP
# Author: Ordan Santos
# Coloque as 'pastas com os input/output' e 'seus codigos' na 'mesma pasta do script'
# Adicione o nome dos problemas como parametro da funcao 'pontos' (veja as ultimas linhas)

import os
import filecmp
import os.path
import signal
import subprocess

import subprocess, threading


class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
            self.process = subprocess.Popen(self.cmd, shell=True, preexec_fn=os.setsid)
            self.process.communicate()

        thread = threading.Thread(target=target)
        thread.daemon = False
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            os.killpg(self.process.pid, signal.SIGTERM)
            thread.join()
        return self.process.returncode

def pontos (nome_problema):
	print ''
	if not os.path.isfile(nome_problema+".py"): 
		print nome_problema + ': 0'
		return 0
	print nome_problema
	exe = "python " + nome_problema + ".py"
	total = 0	

	max_point = 0
	for i in range (1, 11):
		pontuacao_teste = 0
		passou_teste = True
		tle = False
		runtime = False
		point = False
		for j in range (1, 11):
			dir = nome_problema + "/" + str(i) + "/"
			if not os.path.isfile(dir+ "in" + str(j)): break;
			point = True
			command = Command(exe + " < " + dir + "in" + str(j) + " > out")
			code = command.run(timeout=3)

			if code == 0:
				file1 = "out"
				file2 = dir + "out" + str(j)
				if (not filecmp.cmp(file1, file2)): 
					passou_teste = False
			if code == -15: tle = True
			if code == 139: runtime = True
			if code != 0: passou_teste = False
		if not point: continue;
		max_point += 10
		print 'caso: ' + str(i) + ': ',
		
		if passou_teste and not tle and not runtime: 
			total+=10
			print 10,
		else:
			print 0,
		if (tle): print 'TLE',
		if (runtime): print 'Erro em tempo de execucao';
		print ''

	total = (total * 100) / max_point
	print "Total: " + str(total)
	return total

pontuacao = 0
pontuacao += pontos ("arquivos")
pontuacao += pontos ("fita")
pontuacao += pontos ("linhas")
pontuacao += pontos ("mobile")
print 'Total ' + str(pontuacao) 


