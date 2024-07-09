"""Desenvolva um programa que recebe um número e apresente N números de fibonacci"""

print('\033[1;31m-=-\033[m' * 30)
print('FIBONACCI')
print('\033[1;31m-=-\033[m' * 30)

num = int(input('Digite quantos números da sequência de fibonacci deseja ver: '))

anterior = 1
atual = 0
cont = 0

while cont < num:
    print(atual, end=' -> ')
    reserva = atual
    atual = anterior + atual
    anterior = reserva
    cont += 1

print('Acabou')
print('\033[1;31m-=-\033[m' * 30)