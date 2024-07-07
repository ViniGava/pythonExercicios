"""Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0
com uma pause de 1 segundo entre eles"""

from time import sleep

print('\033[1;31m-=-\033[m'*30)
print('CONTAGEM REGRESSIVA\nPARA O ESTOURO DOS FOGOS')
print('\033[1;31m-=-\033[m'*30)

for c in range(10, -1, -1):
    print('Os estouros dos fogos vão acontecer em {}'.format(c))
    sleep(1)
print('\033[1;31mBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM\033[m')
print('\033[1;31m-=-\033[m'*30)