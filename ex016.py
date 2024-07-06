"""Desenvolva um programa utilizando uma biblioteca que informa a parte inteira de um número real digitado"""

import math

print('\033[1;31m-=-\033[m'*30)
num = float(input('Digite um numéro real: '))
print('O numéro real digitado foi: {}, sua parte inteira é: {}'.format(num, math.floor(num)))
print('\033[1;31m-=-\033[m'*30)
