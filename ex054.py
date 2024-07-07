"""Crie um programa que leia o ano de nascimento de 07 pessoas e no final mostre quantas ainda não atingiram a
maioridade e quantas já são maiores"""

from datetime import date

print('\033[1;31m-=-\033[m'*30)
print('MAIORIDADE')
print('\033[1;31m-=-\033[m'*30)

anoatual = date.today().year
menor = 0
maior = 0

for c in range(1, 8):
    idade = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if anoatual - idade >= 21:
        maior += 1
    else:
        menor += 1

print('Dentre os 07 anos citados, {} já completaram 18 anos, e {} faltam completar!!!'.format(maior, menor))

print('\033[1;31m-=-\033[m' * 30)
