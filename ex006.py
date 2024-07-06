"""Desenvolva um programa que leia um número e informe seu dobro, seu triplo e sua raiz quadrada! """

print('\033[1;31m-=-\033[m'*30)
num = int(input('Digite um número: '))
print('Número digitado: \033[1;40m{}\033[m \nO dobro é: \033[1;40m{}\033[m\nO triplo é: \033[1;40m{}\033[m  \nSua raiz quadrada é: \033[1;40m{:.2f}\033[m'.format(num, num*2, num*3, num**(1/2)))
print('\033[1;31m-=-\033[m'*30)