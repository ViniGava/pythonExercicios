"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo"""

print('\033[1;31m-=-\033[m'*30)
print('NÚMERO É PRIMO?')
print('\033[1;31m-=-\033[m'*30)

num = int(input('Digite um número para saber se ele é um NÚMERO PRIMO ou não: '))
primo = 1
if num <= 1:
    print('\033[1;31mO NÚMERO {} NÃO É PRIMO!!!\033[m'.format(num))
else:
    for c in range(2, num):
        if num % c == 0:
            print('\033[1;31mO NÚMERO {} NÃO É PRIMO!!!\033[m'.format(num))
            primo = 0
            break
    if primo == 1:
        print('\033[1;32mO NÚMERO {} É PRIMO!!!\033[m'.format(num))
print('\033[1;31m-=-\033[m' * 30)