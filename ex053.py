"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo"""

import unidecode

print('\033[1;31m-=-\033[m'*30)
print('PALÍNDROMO OU NÃO?')
print('\033[1;31m-=-\033[m'*30)

frase = str(input('Digite uma frase qualquer: ').strip())
frasenova = unidecode.unidecode(frase).replace(' ', '').upper()
fraseinvertida = frasenova[::-1]

print('O inverso de {} é {}!'.format(frasenova, fraseinvertida))

if fraseinvertida == frasenova:
    print('\033[1;32mA frase: {}. É UM PALÍNDROMO\033[m'.format(frase))
else:
    print('\033[1;31mA frase: {}. NÃO É UM PALÍNDROMO\033[m'.format(frase))

print('\033[1;31m-=-\033[m'*30)
