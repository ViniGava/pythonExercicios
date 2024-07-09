"""Desenvolva um jogo de adivinhação onde o computador vai escolher um número aleátorio entre 1 e 10 e o usuário tenta
acertar qual será o número escolhido"""
from random import randint
from time import sleep

print('\033[1;31;40m-=-\033[m'*30)
print('\033[1;31mBem Vindo ao jogo de adivinhação 1.0\033[m')
print('\033[1;31mO computador sorteará um número aleátorio entre 0 e 10, tente adivinhar qual será!!!\033[m')
print('\033[1;31;40m-=-\033[m'*30)

cont = 1
r = 1
numusuario = 00
while True:

    numsorteado = randint(0, 10)
    numusuario = input('Digite um número entre 0 e 10: ')
    if numusuario == '':
        print('\033[1;31mNÚMERO INVÁLIDO\033[m')
        continue
    if not numusuario.isnumeric():
        print('\033[1;31mNÚMERO INVÁLIDO\033[m')
        continue
    else:
        numusuario = int(numusuario)

    if numusuario > 10:
        print('\033[1;31mNÚMERO INVÁLIDO\033[m')
        continue


    print('\033[4;33;40mPROCESSANDO................\033[m')
    sleep(1)

    print('-' * 30)
    print(f'\n\n\033[1;31mO número sorteado foi {numsorteado}\033[m')
    print(f'\033[1;32mO número digitado foi {numusuario}\033[m\n\n')
    print('-' * 30)

    if numusuario == numsorteado:
        print('\033[1;32;40mPARABÉNSSSS você adivinhou o número!!!!!!!\033[m\n\n')
        break
    else:
        print('\033[1;31;40mInfelizmente você errou!!!! TENTE DE NOVO\033[m\n\n')
        cont += 1
        continue

print(f'\033[1;33mVocê precisou de {cont} tentativas para acertar!!!\033[m\n')

print('\033[1;31;40m-=-\033[m'*30)
print('\033[1;31mFim do jogo de adivinhação 1.0\033[m')
print('\033[1;31;40m-=-\033[m'*30)
