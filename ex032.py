"""Desenvolva um programa que recebe um ano pelo teclado, e informa se tal no é bissexto"""

from datetime import date

print('='*30)
print('Ano Bissexto?????\n')
ano = int(input('Digite o ano para saber se ele é bissexto (0 para ano atual): '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0) & (ano % 100 != 0) or (ano % 400 == 0) & (ano % 100 == 0):
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('A ano {} não é BISSEXTO!'.format(ano))
print('\033[1;31m-=-\033[m'*30)
