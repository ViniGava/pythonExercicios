"""Refaça o desafio 61 (Desenvolva um programa que leia o primeiro termo e a razão de uma progressão
 aritmética, no final mostre os 10 termos dessa progressão) usando while e perguntando para
 o usuário se ele quer continuar"""



print('\033[1;31m-=-\033[m'*30)
print('PROGRESSÃO ARITMÉTICA')
print('\033[1;31m-=-\033[m'*30)

termo = int(input('Digite o PRIMEIRO TERMO da progressão aritmética: '))
razao = int(input('Digite a razão a ser seguida: '))
r = 1
c = 1
termofim = 11
soma = 10
while r != 0:
    while c < termofim:
       print(termo, end=' -> ')
       c += 1
       termo += razao
    print('Pausa')
    r = int(input('\nDeseja ver mais quantos termos? [0] PARA SAIR: '))
    if r > 0:
        termofim = r + 1
        c = 1
    soma += r

print('\033[1;31m-=-\033[m'*30)
print('\nA quantidade de termos mostrado foi de: {}.\n'.format(soma))
print('\033[1;31m-=-\033[m'*30)