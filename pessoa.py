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
		if p[1][0] > 0:
			arrPosAntiga = p[1]
			p[1][0] = p[1][0]-1
			p[1] = alterarAmbiente(arrPosAntiga, p[1])
		if p[1][1] > 0:
			arrPosAntiga = p[1]
			p[1][1] = p[1][1]-1
			p[1] = alterarAmbiente(arrPosAntiga, p[1])
		if p[1][0] < amb.len(mAmbiente)-1:
			arrPosAntiga = p[1]
			p[1][0] = p[1][0]+1
			p[1] = alterarAmbiente(arrPosAntiga, p[1])
		if p[1][1] < amb.len(mAmbiente[0])-1:
			arrPosAntiga = p[1]
			p[1][1] = p[1][1]+1
			p[1] = alterarAmbiente(arrPosAntiga, p[1])
		print("Pessoa {}, posicao é {}".format(p[0],p[1]))
		time.sleep(2.1)
	andarPessoaPorta(p)

def andarPessoaPorta(p):
	portaPessoa = p[1]
	# igualar o x da pessoa ao da porta
	# igualar o y da pessoa ao da porta
	print('andou porta, %s' % (p[0]))
