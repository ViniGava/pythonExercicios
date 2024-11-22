"""Desenvolva um programa que tenha uma lista chamada numeros, e duas function chamadas sorteia() e somaPar()A primeira funct vai sortear 5 números e vai colocá-los dentro da lista e a segunda vai mostar a soma entre todos os valores sorteados."""

print('\033[1;31m=\033[m' * 40)
print(f'{'Sortear e Somar':^40}')
print('\033[1;31m=\033[m' * 40)

from time import sleep
from random import choices

def sorteia(num):
  sorteados = []
  print('Sorteando 5 valores da lista: ', end=' ')
  for n in num:
    print(n, end=' ', flush=True)
    sleep(.5)
    sorteados.append(n)
  print('PRONTO!')
  somaPar(sorteados)

def somaPar(num):
  pares = 0
  for n in num:
    if n % 2 == 0:
      pares += n
  print(f'Somando os valores pares de {num}, temos {pares}')

numeros = list(range(0,11))

sorteia(choices(numeros, k=5))

print('\033[1;31m=\033[m' * 40)