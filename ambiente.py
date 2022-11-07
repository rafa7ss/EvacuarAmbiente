import time
import os
import random
import threading

global mAmbiente, larguraAmbiente, comprimentoAmbiente, nPessoas, nPortas, arrPortas, arrPessoas

mAmbiente = False
larguraAmbiente = False
comprimentoAmbiente = False
nPessoas = False
nPortas = False
arrPortas = False
arrPessoas = False

def preencherAmbiente():
	mAmbiente = [[r"[ ]" for x in range(larguraAmbiente)] for y in range(comprimentoAmbiente)]
	return mAmbiente

def preencherAmbientePortas():
	arrPortas = []
	for i in range(0, nPortas):
		sucesso = False
		while not sucesso:
			x = random.randint(0,len(mAmbiente)-1)
			if(x in (0,len(mAmbiente)-1)):
				y = random.randint(1,len(mAmbiente[0])-2)
			else:
				y = random.choice([0,len(mAmbiente[0])-1])
			if(mAmbiente[x][y] == "[ ]"):
				sucesso = True
				mAmbiente[x][y] = "[P]"
				arrPortas.append([x,y])

		imprimirMatriz()
	return mAmbiente, arrPortas

def preencherAmbientePessoas():
	arrPessoas = []
	for i in range(0, nPessoas):
		sucesso = False
		while not sucesso:
			x = random.randint(0,len(mAmbiente)-1)
			if(x not in (0,len(mAmbiente)-1)):
				y = random.randint(1,len(mAmbiente[0])-2)
				if(mAmbiente[x][y] == "[ ]"):
					sucesso = True
					mAmbiente[x][y] = "[*]"
					arrPessoas.append([i, [x,y], escolherPorta()])

		imprimirMatriz()
	return mAmbiente, arrPessoas

def alterarAmbiente(arrPosAntiga, arrPosAtual):
	if mAmbiente[arrPosAtual[0],arrPosAtual[1]] not in ['[P]','[*]']:
		mAmbiente[arrPosAntiga[0],arrPosAntiga[1]] = '[ ]'
		imprimirMatriz()
		return arrPosAtual
	else:
		time.sleep(random.randint(0.1,3))
		return arrPosAntiga

def imprimirMatriz():
	time.sleep(0.2)
	os.system('cls') or None
	for l in mAmbiente:
	    for v in l:
	        print(" "+v+" ", end="")
	    print()

def escolherPorta():
	return random.choice(arrPortas)