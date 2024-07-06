"""Desenvolva um programa que receba 3 segmentos de reta e retorne se é possível ou não formar um triângulo"""

print('\033[1;31m-=-\033[m'*30)
r1 = float(input('Digite o comprimento do 1º segmento: '))
r2 = float(input('Digite o comprimento do 2º segmento: '))
r3 = float(input('Digite o comprimento do 3º segmento: '))

if (r1 + r2 > r3) & (r1 + r3 > r2) & (r2 + r3 > r1):
    print('Com os segmentos {:.1f}, {:.1f}, {:.1f} é possível formar um triângulo!!!'.format(r1, r2, r3))
else:
    print('Com os segmentos {:.1f}, {:.1f}, {:.1f} não é possível formar um triângulo!!!'.format(r1, r2, r3))
print('\033[1;31m-=-\033[m' * 30)
