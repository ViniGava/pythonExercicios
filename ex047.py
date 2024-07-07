"""Crie um programa que mostre na tela todos os números para que estão entre 1 e 50"""

print('\033[1;31m-=-\033[m'*30)
print('NÚMEROS PARES ENTRE 1 E 50')
print('\033[1;31m-=-\033[m'*30)

print('Os números pares existentes entre 1 e 50 são: ')
for c in range(1, 51, 2):
    print(c + 1, end=', ')
print('Acabou')
print('\033[1;31m-=-\033[m'*30)