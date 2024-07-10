"""Desenvolva um programa que leia quatro valores pelo teclado e guarde em uma tupla, no final mostre quantas
vezes apareceu o número 9, em que posição foi digitado o primeiro valor 3 e quantos são pares"""

print('\033[1;31m=\033[m' * 40)
print(f'{'ÁNALISE DE DADOS EM TUPLA':^40}')
print('\033[1;31m=\033[m' * 40)

valores = (int(input('Digite o primeiro valor: ')),
           int(input('Digite o segundo valor: ')),
           int(input('Digite o terceiro valor: ')),
           int(input('Digite o quarto valor: ')))

num3 = numeropar = 0
num = 'números'

print(f'Você digitou os valores {valores}!')
print(f'O valor 9 apareceu {valores.count(9)} vezes!')

for numero in valores:
    if numero == 3:
        num3 = 1
    if numero % 2 == 0:
        numeropar = 1

if num3 >= 1:
    print(f'O valor 3 apareceu primeiramente na {valores.index(3) + 1} posição!')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

if numeropar == 1:
    print('Os valores pares digitados foram:', end=' ')
    for numpar in valores:
        if numpar % 2 == 0:
            print(numpar, end=' ')
else:
    print('Não foi digitado nenhum número par')
print('')
print('\033[1;31m=\033[m' * 40)
