"""Crie um programa que leia vários números e só pare quando o usúario digitar 999, no final
mostre a quantidade de números digitados e a soma deles"""

print('\033[1;31m-=-\033[m'*30)
print('SOMADOR DE NÚMEROS')
print('\033[1;31m-=-\033[m'*30)

r = 0
soma = 0
cont = 0

while r != 999:
    r = int(input('Digite um valor! [999] PARA SAIR: '))
    if r != 999:
        cont += 1
        soma = soma + r
print('Você digitou {} números e a soma deles é de: {}'.format(cont, soma))
print('Programa Encerrado')
print('\033[1;31m-=-\033[m'*30)