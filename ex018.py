"""Desenvolva um programa que calcule o seno, cosseno, e tangente de um número recebido pelo teclado"""

import math

print('\033[1;31m-=-\033[m'*30)
ang = int(input('Digite o ângulo para saber seu seno, cosseno e tangente: '))
rad = math.radians(ang)
print('Ângulo: {}º\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(ang, math.sin(rad), math.cos(rad), math.tan(rad)))
print('\033[1;31m-=-\033[m'*30)
