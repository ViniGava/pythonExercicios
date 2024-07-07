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

while r != 0:
    numusuario = int(input('Digite um número entre 0 e 10: '))
    numsorteado = randint(0, 10)

    print('\033[4;33;40mPROCESSANDO................\033[m')
    sleep(2)
    print('-' * 30)
    print('O número sorteado foi {}'.format(numsorteado))
    print('O número digitado foi {}'.format(numusuario))
    print('-' * 30)

    if numusuario == numsorteado:
        print('\033[1;32;40mPARABÉNSSSS você adivinhou o número!!!!!!!\033[m\n\n')
        r = 0
    else:
        print('\033[1;31;40mInfelizmente você errou!!!! TENTE DE NOVO\033[m\n\n')
        r = 1
        cont += 1

print('Você precisou de {} tentativas para acertar!!!'.format(cont))
print('-=-'*30)
print('Fim do jogo de adivinhação 1.0')
print('-=-'*30)
