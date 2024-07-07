"""Desenvolva um programa que recebe um número e apresente N números de fibonacci"""

print('\033[1;31m-=-\033[m' * 30)
print('FIBONACCI')
print('\033[1;31m-=-\033[m' * 30)

num = int(input('Digite quantos números da sequência de fibonacci deseja ver: '))

anterior = 1
atual = 0

for c in range(0, num):
    print(atual, end=' ')
    reserva = atual
    atual = anterior + atual
    anterior = reserva


print('Acabou')
print('\033[1;31m-=-\033[m' * 30)