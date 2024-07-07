"""Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética, no final mostre os 10 termos
dessa progressão."""

print('\033[1;31m-=-\033[m'*30)
print('PROGRESSÃO ARITMÉTICA')
print('\033[1;31m-=-\033[m'*30)

termo = int(input('Digite o PRIMEIRO TERMO da progressão aritmética: '))
razao = int(input('Digite a razão a ser seguida: '))
termofim = termo + 10 * razao

for c in range(termo, termofim, razao):
    print(c, end=' -> ')
print('Acabou')
print('\033[1;31m-=-\033[m'*30)