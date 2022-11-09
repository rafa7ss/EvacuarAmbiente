import time
import os
import random
import threading

import pessoa as p

# global mAmbiente, larguraAmbiente, comprimentoAmbiente, nPessoas, nPortas, arrPortas, arrPessoas, timerAmb
global timer
timer = False

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

		time.sleep(0.3)
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

		time.sleep(0.3)
		imprimirMatriz()

	return mAmbiente, arrPessoas

def alterarAmbiente(arrPosAntiga, arrPosAtual, arrPortaPessoa = False):
	if not arrPortaPessoa:
		if mAmbiente[arrPosAtual[0]][arrPosAtual[1]] not in ['[P]','[*]']:
			mAmbiente[arrPosAntiga[0]][arrPosAntiga[1]] = '[ ]'
			mAmbiente[arrPosAtual[0]][arrPosAtual[1]] = '[*]'
			imprimirMatriz()
			time.sleep(random.randint(1,2))
			return arrPosAtual
		else:
			time.sleep(random.randint(1,2))
			return arrPosAntiga
	elif mAmbiente[arrPosAtual[0]][arrPosAtual[1]] not in ['[P]','[*]']:
		mAmbiente[arrPosAntiga[0]][arrPosAntiga[1]] = '[ ]'
		mAmbiente[arrPosAtual[0]][arrPosAtual[1]] = '[*]'
		imprimirMatriz()
		time.sleep(random.randint(1,2))
		return arrPosAtual
	elif mAmbiente[arrPosAtual[0]][arrPosAtual[1]] == '[*]':
		arrNovaPosAtual = []
		andou = False
		while(not andou):
			ranInt = random.choice([1,2,3,4])
			if ranInt == 1 and arrPosAntiga[0]-1 >= 0 and mAmbiente[arrPosAntiga[0]-1][arrPosAntiga[1]] not in ['[*]', '[P]']:
				arrNovaPosAtual = [arrPosAntiga[0]-1,arrPosAntiga[1]]
				mAmbiente[arrPosAntiga[0]][arrPosAntiga[1]] = '[ ]'
				mAmbiente[arrNovaPosAtual[0]][arrNovaPosAtual[1]] = '[*]'
				imprimirMatriz()
				andou = True
			elif ranInt == 2 and arrPosAntiga[0]+1 <= len(mAmbiente[0])-1 and mAmbiente[arrPosAntiga[0]+1][arrPosAntiga[1]] not in ['[*]', '[P]']:
				arrNovaPosAtual = [arrPosAntiga[0]+1,arrPosAntiga[1]]
				mAmbiente[arrPosAntiga[0]][arrPosAntiga[1]] = '[ ]'
				mAmbiente[arrNovaPosAtual[0]][arrNovaPosAtual[1]] = '[*]'
				imprimirMatriz()
				andou = True
			elif ranInt == 3 and arrPosAntiga[1]-1 >= 0 and mAmbiente[arrPosAntiga[0]][arrPosAntiga[1]-1] not in ['[*]', '[P]']:
				arrNovaPosAtual = [arrPosAntiga[0],arrPosAntiga[1]-1]
				mAmbiente[arrPosAntiga[0]][arrPosAntiga[1]] = '[ ]'
				mAmbiente[arrNovaPosAtual[0]][arrNovaPosAtual[1]] = '[*]'
				imprimirMatriz()
				andou = True
			elif ranInt == 4 and arrPosAntiga[1]+1 <= len(mAmbiente[0][0])-1 and mAmbiente[arrPosAntiga[0]][arrPosAntiga[1]+1] not in ['[*]', '[P]']:
				arrNovaPosAtual = [arrPosAntiga[0],arrPosAntiga[1]+1]
				mAmbiente[arrPosAntiga[0]][arrPosAntiga[1]] = '[ ]'
				mAmbiente[arrNovaPosAtual[0]][arrNovaPosAtual[1]] = '[*]'
				imprimirMatriz()
				andou = True
		return arrNovaPosAtual
	else:
		mAmbiente[arrPosAntiga[0]][arrPosAntiga[1]] = '[ ]'
		imprimirMatriz()
		while(mAmbiente[arrPosAtual[0]][arrPosAtual[1]] == '[*]'):
			time.sleep(1)
		return arrPortaPessoa

def imprimirMatriz():
	global timer
	while(timer):
		time.sleep(0.5)
	timer = True
	os.system('cls') or None
	for l in mAmbiente:
	    for v in l:
	        print(" "+v+" ", end="")
	    print()
	timer = False
	print('Threads: {}'.format(threading.active_count()-1))

def escolherPorta():
	return random.choice(arrPortas)