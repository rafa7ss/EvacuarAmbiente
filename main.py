import os
import time
import threading
# import keyboard

import ambiente as amb
import pessoa as p

# print("Digite a largura do ambiente:")
# amb.larguraAmbiente = int(input())
# print("Digite o comprimento do ambiente:")
# amb.comprimentoAmbiente = int(input())
# print("Digite o número de portas:")
# amb.nPortas = int(input())
# print("Digite o número de pessoas:")
# amb.nPessoas = int(input())

amb.larguraAmbiente = 10
amb.comprimentoAmbiente = 10
amb.nPortas = 1
amb.nPessoas = 15

amb.mAmbiente = amb.preencherAmbiente()

amb.imprimirMatriz()

amb.mAmbiente, amb.arrPortas = amb.preencherAmbientePortas()

amb.mAmbiente, amb.arrPessoas = amb.preencherAmbientePessoas()

for arrPessoa in amb.arrPessoas:
	thread = threading.Thread(target=p.criarPessoa, args=(arrPessoa,), daemon=True)
	thread.start()

# while(not keyboard.read_key() == 'enter'):
	# time.sleep(0.1)

time.sleep(1)

p.timer = False

while(len(amb.arrPessoas) > 0):
	time.sleep(0.1)
amb.imprimirMatriz()
print('Terminou!')