import time

import ambiente as amb

global timer
timer = True

def criarPessoa(p):
	controlarPessoa(p)

def controlarPessoa(p):
	andarPessoaAleatoriamente(p)

def andarPessoaAleatoriamente(p):
	while(timer):
		time.sleep(0.1)
	andarPessoaPorta(p)

def andarPessoaPorta(p):
	# igualar o x da pessoa ao da porta
	# igualar o y da pessoa ao da porta
	print('andou porta, %s' % (p[0]))
