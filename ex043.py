"""Desenvolva um programa que calcule o IMC de uma pessoa"""

print('\033[1;31m-=-\033[m'*30)
print('ÍNDICE DE MASSA CORPORAL')
print('\033[1;31m-=-\033[m'*30)

peso = int(input('Digite o peso em Kg: '))
altura = float(input('Digite a altura em M: '))
imc = peso/(altura ** 2)

if imc < 18.5:
    status = 'ABAIXO DO PESO'
    corinicio = '\033[1;31m'
    corfim = '\033[m'
elif imc < 25:
    status = 'PESO IDEAL'
    corinicio = '\033[1;32m'
    corfim = '\033[m'
elif imc < 30:
    status = 'SOBREPESO'
    corinicio = '\033[1;33m'
    corfim = '\033[m'
elif imc < 40:
    status = 'OBESIDADE'
    corinicio = '\033[1;31m'
    corfim = '\033[m'
else:
    status = 'OBESIDADE MÓRBIDA'
    corinicio = '\033[1;31m'
    corfim = '\033[m'

print('O IMC É {:.2f} E O STATUS É {}{}{}!!!'.format(imc, corinicio, status, corfim))


print('\033[1;31m-=-\033[m'*30)