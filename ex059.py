"""Crie um programa que leia 2 valores e mostre um menu na tela"""

print('\033[1;31;40m-=-\033[m' * 30)
print('O QUE FAZER COM 2 NÚMEROS????')
print('\033[1;31;40m-=-\033[m' * 30)

r = 1

while r != 5:
    n1 = float(input('Digite o 1º valor: '))
    n2 = float(input('Digite o 2º valor: '))
    r = int(input('''----------- MENU ----------
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR
    OPÇÃO: '''))

    if r == 1:
        result = n1 + n2
        print('A soma dos números {} e {} é igual à: {}'.format(n1, n2, result))
    elif r == 2:
        result = n1 * n2
        print('A multiplicação de {} com {} é igual à: {}'.format(n1, n2, result))
    elif r == 3:
        if n1 > n2:
            print('O {} é maior que {}!'.format(n1, n2))
        else:
            print('O {} é maior que {}'.format(n2, n1))

print('Programa finalizado com sucesso')




print('\033[1;31;40m-=-\033[m' * 30)
