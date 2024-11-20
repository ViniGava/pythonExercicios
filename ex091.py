"""Criem um programa, onde 4 jogadores lançam um dado e tenham resultados aleátorios. Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número..."""

print('\033[1;31m=\033[m' * 40)
print(f'{'Aleatorizando Dados':^40}')
print('\033[1;31m=\033[m' * 40)

from random import randint
from time import sleep

c = 1
jogo = {}

for j in range(1,5):
  jogo[f'jogador{j}'] = randint(1,6)

print('== Valores Sorteados ==')
for k, i in jogo.items():
  sleep(1)
  print(f'   O {k} tirou {i}')

jogosort = dict(sorted(jogo.items(), key=lambda item: item[1], reverse=True))

print('\033[1;31m-\033[m' * 40)
print('== Ranking dos Jogadores ==')
for k, i in jogosort.items():
  sleep(1)
  print(f'   {c}o Lugar: {k} com {i}')
  c += 1

print('\033[1;31m=\033[m' * 40)