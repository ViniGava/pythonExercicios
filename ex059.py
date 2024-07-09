"""Crie um programa que leia 2 valores e mostre um menu na tela"""

print('\033[1;31;40m-=-\033[m' * 30)
print('\033[1;31mO QUE FAZER COM 2 NÚMEROS????\033[m')
print('\033[1;31;40m-=-\033[m' * 30)

r = 4

while r != 5:
    if r == 4:
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
    r = int(input('''\033[1;33m----------- MENU ----------
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR\033[m
>>>>>> OPÇÃO: '''))

    if r == 1:
        result = n1 + n2
        print('\033[1;32mA soma dos números {} + {} é igual à: {}!\033[m'.format(n1, n2, result))
    elif r == 2:
        result = n1 * n2
        print('\033[1;32mA multiplicação de {} * {} é igual à: {}!\033[m'.format(n1, n2, result))
    elif r == 3:
        if n1 > n2:
            print('\033[1;32mO maior entre {} e {} é {}!\033[m'.format(n1, n2, n1))
        else:
            print('\033[1;32mO maior entre {} e {} é {}!\033[m'.format(n1, n2, n2))
    elif r > 6 or r < 1:
        print('\033[1;31mOPÇÃO INVÁLIDA\033[m')

print('\033[1;31;40m-=-\033[m' * 30)
print('\033[1;31mPrograma finalizado com sucesso\033[m')
print('\033[1;31;40m-=-\033[m' * 30)
