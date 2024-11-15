"""Faça um programa que ajude um jogador da mega sena a criar palpites, O programa vai perguntar quantos jogos serao gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando em uma lista composta."""

from time import sleep
from random import sample

print('\033[1;31m=\033[m' * 40)
print(f'{'MEGA SENA HELPER':^40}')
print('\033[1;31m=\033[m' * 40)

numeros = list(range(0,61))
jogos = []

qtdjogos = int(input('\nQuantos jogos voce quer que eu sorteie? '))
sleep(.8)

print(f'\n\033[1;31m========== SORTEANDO {qtdjogos} JOGOS ==========\033[m\n')

for cont in range (0, qtdjogos):
  sleep(.4)
  jogos = sample(numeros, k=6)
  jogos.sort()
  print(f'JOGO {cont+1}: {jogos}')
  jogos.clear()

print('\033[1;31m=\033[m' * 40)