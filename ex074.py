"""Coloque 5 números aleatórios dentro de uma tupla, depois mostre-os, e mostre também o maior e o menos valor gerado"""

print('\033[1;31m=\033[m' * 40)
print(f'{'MAIOR E MENOR EM TUPLA':^40}')
print('\033[1;31m=\033[m' * 40)

from random import randint

maiorvalor = menorvalor = 0

tupla = (randint(0, 100), randint(0, 100), randint(0, 100),
         randint(0, 100), randint(0, 100))

for cont in range(0, len(tupla)):
    if cont == 1:
        maiorvalor = tupla[0]
        menorvalor = tupla[0]
    if tupla[cont] > maiorvalor:
        maiorvalor = tupla[cont]
    if tupla[cont] < menorvalor:
        menorvalor = tupla[cont]

print(f'Os números sorteados foram: {tupla}')
print(f'O maior número sorteado foi: {maiorvalor}')
print(f'O menor número sorteado foi: {menorvalor}')

print('\033[1;31m=\033[m' * 40)
