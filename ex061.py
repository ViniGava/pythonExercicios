"""Refaça o desafio 51 (Desenvolva um programa que leia o primeiro termo e a razão de uma progressão
 aritmética, no final mostre os 10 termos dessa progressão) usando while"""



print('\033[1;31m-=-\033[m'*30)
print('PROGRESSÃO ARITMÉTICA')
print('\033[1;31m-=-\033[m'*30)

termo = int(input('Digite o PRIMEIRO TERMO da progressão aritmética: '))
razao = int(input('Digite a razão a ser seguida: '))
c = 1
while c < 11:
   print(termo, end=' -> ')
   c += 1
   termo += razao
print('Acabou')
print('\033[1;31m-=-\033[m'*30)