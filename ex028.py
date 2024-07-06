from random import randint
from time import sleep

print('\033[1;31;40m-=-\033[m'*30)
print('\033[1;31mBem Vindo ao jogo de advinhação 1.0\033[m')
print('\033[1;31mO computador sorteará um número aleátorio entre 0 e 5, tente advinhar qual será!!!\033[m')
print('\033[1;31;40m-=-\033[m'*30)

numusuario = int(input('Digite um número entre 0 e 5: '))
numsorteado = randint(0, 5)

print('\033[4;33;40mPROCESSANDO................\033[m')
sleep(2)
print('O número sorteado foi {}'.format(numsorteado))

if numusuario == numsorteado:
    print('\033[1;32;40mPARABÉNSSSS você advinhou o número!!!!!!!\033[m\n\n')
else:
    print('\033[1;31;40mInfelizmente você errou!!!! Mais sorte da proxima vez\033[m\n\n')

print('-=-'*30)
print('Fim do jogo de advinhação 1.0')
print('-=-'*30)