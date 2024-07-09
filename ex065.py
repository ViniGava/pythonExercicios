"""Crie um programa que lê vários números pelo teclado e mostre a média deles, qual foi
o maior e qual o menor, perguntar se o usúario quer continuar"""

print('\033[1;31m-=-\033[m'*30)
print('Média')
print('\033[1;31m-=-\033[m'*30)

r = 's'
soma = 0
cont = 0
nummaior = 0
nummenor = 0


while r != 'n':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        nummaior = num
        nummenor = num
    if num > nummaior:
        nummaior = num
    if num < nummenor:
        nummenor = num
    r = str(input('Deseja continuar? [S/N]')).strip().lower()

media = soma / cont

print('\033[1;32mA quantidade de números somados foi de: {} e a média entre ele é: {}\033[m'.format(cont, media))
print('\033[1;33mO maior número digitado foi {}, e o menor foi {}!\033[m'.format(nummaior, nummenor))

print('\033[1;31m-=-\033[m'*30)