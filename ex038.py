"""Desenvolva um programa que recebe 2 números e faça uma comparação indicando qual o maior ou se os 2 são iguais"""

print('\033[1;31m-=-\033[m'*30)
print('COMPARAÇÃO ENTRE DOIS NÚMEROS')
print('\033[1;31m-=-\033[m'*30)

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º numero: '))

if n1 > n2:
    print('O número {} é maior que {}!'.format(n1, n2))
elif n1 < n2:
    print('O número {} é maior que {}!'.format(n2, n1))
else:
    print('Não tem número maior, os 2 números são iguais!!!')

print('\033[1;31m-=-\033[m' * 30)
