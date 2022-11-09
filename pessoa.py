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
			PosAntiga = p[1]
			PosAtual = [p[1][0]-1,p[1][1]]
			p[1] = amb.alterarAmbiente(PosAntiga, PosAtual)
		if p[1][1] > 0:
			PosAntiga = p[1]
			PosAtual = [p[1][0],p[1][1]-1]
			p[1] = amb.alterarAmbiente(PosAntiga, PosAtual)
		if p[1][0] < len(amb.mAmbiente)-1:
			PosAntiga = p[1]
			PosAtual = [p[1][0]+1,p[1][1]]
			p[1] = amb.alterarAmbiente(PosAntiga, PosAtual)
		if p[1][1] < len(amb.mAmbiente[0])-1:	
			PosAntiga = p[1]
			PosAtual = [p[1][0],p[1][1]+1]
			p[1] = amb.alterarAmbiente(PosAntiga, PosAtual)
		time.sleep(0.1)
	andarPessoaPorta(p)

def andarPessoaPorta(p):
	PosAtual = p[1]
	portaPessoa = p[2]
	while(p[1] != p[2]):
		# igualar o x da pessoa ao da porta
		if p[1][0] != p[2][0]:
			if p[1][0] > p[2][0]:
				PosAntiga = p[1]
				PosAtual = [p[1][0]-1,p[1][1]]
				p[1] = amb.alterarAmbiente(PosAntiga, PosAtual, p[2])
			else:
				PosAntiga = p[1]
				PosAtual = [p[1][0]+1,p[1][1]]
				p[1] = amb.alterarAmbiente(PosAntiga, PosAtual, p[2])
		# igualar o y da pessoa ao da porta
		else:
			if p[1][1] > p[2][1]:
				PosAntiga = p[1]
				PosAtual = [p[1][0],p[1][1]-1]
				p[1] = amb.alterarAmbiente(PosAntiga, PosAtual, p[2])
			else:
				PosAntiga = p[1]
				PosAtual = [p[1][0],p[1][1]+1]
				p[1] = amb.alterarAmbiente(PosAntiga, PosAtual, p[2])
	amb.arrPessoas.remove(p)