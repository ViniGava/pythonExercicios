"""Desenvolva um programa que leia 06 números inteiros, e some aqueles que forem pares, os ímpares desconsidere"""

print('\033[1;31m-=-\033[m'*30)
print('SOMADOR DE NÚMEROS')
print('\033[1;31m-=-\033[m'*30)
soma = 0
pares = 0

for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        soma += num
        pares += 1

print('Você digitou {} números pares e a soma deles é de: {}.'.format(pares, soma))
print('\033[1;31m-=-\033[m'*30)
