"""Desenvolva um programa onde recebe o ano de nascimento de um atleta e informe qual a categoria dele baseado na sua
idade"""

from datetime import date

print('\033[1;31m-=-\033[m'*30)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('CATEGORIAS')
print('\033[1;31m-=-\033[m'*30)

anoatual = date.today().year
anonasc = int(input('Digite o ano de nascimento do atleta: '))
idade = anoatual - anonasc

if idade > 25:
    categoria = 'MASTER'
elif idade >= 19:
    categoria = 'SÊNIOR'
elif idade >= 14:
    categoria = 'JUNIOR'
elif idade >= 9:
    categoria = 'INFANTIL'
else:
    categoria = 'MIRIM'

print('A idade do atleta é {} anos!'.format(idade))
print('A CATEGORIA DO ATLETA SERÁ \033[1;32m{}\033[m!'.format(categoria))
print('\033[1;31m-=-\033[m'*30)