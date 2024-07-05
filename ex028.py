from random import randint
from time import sleep

print('-=-'*30)
print('Bem Vindo ao jogo de advinhação 1.0')
print('O computador sorteará um número aleátorio entre 0 e 5, tente advinhar qual será')
print('-=-'*30)

numusuario = int(input('Digite um número entre 0 e 5: '))
numsorteado = randint(0, 5)

print('PROCESSANDO................')
sleep(2)
print('O número sorteado foi {}'.format(numsorteado))

if numusuario == numsorteado:
    print('PARABÉNSSSS você advinhou o número!!!!!!!\n\n')
else:
    print('Infelizmente você errou!!!! Mais sorte da proxima vez\n\n')

print('-=-'*30)
print('Fim do jogo de advinhação 1.0')
print('-=-'*30)