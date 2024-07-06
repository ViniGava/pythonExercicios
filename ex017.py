"""Desenvolva um programa que calcula a hipotenusa a partir de 2 catetos recebidos do teclado"""

import math

print('\033[1;31m-=-\033[m'*30)
oposto = float(input('Digite o cateto oposto em cm: '))
adj = float(input('Digite o cateto adjacente em cm: '))
print('A hipotenusa é: {:.2f}cm'.format(math.hypot(oposto, adj)))
print('\033[1;31m-=-\033[m'*30)
