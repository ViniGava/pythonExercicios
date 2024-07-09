"""Leia um número qualquer e faça seu fatorial
3 formas de fazer"""

print('\033[1;31;40m-=-\033[m'*30)
print('FATORIAL')
print('\033[1;31;40m-=-\033[m'*30)

'''RESOLVENDO COM A BIBLIOTECA MATH
from math import factorial
num = int(input('Digite um número para saber seu fatorial: '))
print('O fatorial de {}! é : {}'.format(num, factorial(num)))'''

'''RESOLVENDO COM WHILE
num = int(input('Digite um número para saber seu fatorial: '))
numf = num - 1
nums = num
while numf != 1:
    nums = nums * numf
    numf -= 1

print('O fatorial de {}! é : {}'.format(num, nums))'''

#RESOLVENDO COM FOR

num = int(input('Digite um número para saber seu fatorial: '))
numf = num - 1
nums = num
for c in range(num, 1, -1):
    nums = nums * numf
    numf -= 1
print('Calculando {}! = {}'.format(num, nums))