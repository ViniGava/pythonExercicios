"""Desenvolva um programa que recebe 1 número pelo teclado, e mostre seu antecessor e seu sucessor"""

print('\033[1;31m-=-\033[m'*20)
n = int(input('Digite um número: '))
print('Número digitado = {}\nSucessor = \033[1;32m{}\033[m\nAntecessor = \033[1;31m{}\033[m'.format(n, n+1, n-1))
print('\033[1;31m-=-\033[m'*20)
