import os
import time
import threading
import keyboard

import ambiente as amb
import pessoa as p

print("Digite a largura do ambiente:")
amb.larguraAmbiente = int(input())
print("Digite o comprimento do ambiente:")
amb.comprimentoAmbiente = int(input())

print("Digite o número de portas:")
amb.nPortas = int(input())

print("Digite o número de pessoas:")
amb.nPessoas = int(input())

amb.mAmbiente = amb.preencherAmbiente()

amb.imprimirMatriz()

amb.mAmbiente, amb.arrPortas = amb.preencherAmbientePortas()

amb.mAmbiente, amb.arrPessoas = amb.preencherAmbientePessoas()

# p.criarPessoa([])

for arrPessoa in amb.arrPessoas:
	print(arrPessoa)
	thread = threading.Thread(target=p.criarPessoa, args=(arrPessoa,), daemon=False)
	thread.start()

while(not keyboard.read_key() == 'enter'):
	time.sleep(0.1)

p.timer = False