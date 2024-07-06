"""Desenvolva um programa que recebe um número inteiro e informe se ele é PAR ou ÍMPAR"""

print('\033[1;31m-=-\033[m'*30)
num = int(input('Digite um número para saber se é par ou ímpar: '))
if num % 2 == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é ÍMPAR'.format(num))
print('\033[1;31m-=-\033[m'*30)
