"""Jogo PAR OU ÍMPAR que só termina quando o usuario perder, e mostra quantas vitórias consecutivas teve;"""

from random import randint
from time import sleep

print('\033[1;31m-=-\033[m'*30)
print('PAR OU ÍMPAR')
print('\033[1;31m-=-\033[m'*30)

vitorias = 0

while True:
    numusuario = int(input('Digite um número: '))
    r = str(input('Voce quer PAR ou ÍMPAR? [P/I]: ')).strip().upper()[0]
    numcomputador = randint(0, 10)
    sleep(2)
    soma = numusuario + numcomputador
    somanum = soma % 2
    print('\033[1;31m-=-\033[m' * 30)

    print(f'\033[1;32mVocê escolheu {numusuario}\033[m\n\033[1;31mO computador escolheu {numcomputador}\033[m\n\033[1;33mA soma é {soma}\033[m')
    print('\033[1;31m-=-\033[m' * 30)
    if somanum == 0:
        if r in 'Pp':
            ganhador = 1
        else:
            ganhador = 2
    else:
        if r in 'Ii':
            ganhador = 1
        else:
            ganhador = 2

    if ganhador == 1:

        print('\033[1;32mParabéns!!!! Você ganhou\033[m')
        print('\033[1;31m-=-\033[m' * 30)
        print('\nVamos jogar de novo!!!!\n')
        vitorias += 1
    else:
        break


print('\n\033[1;31mInfelizmente você perdeu!\033[m\n')

print('\033[1;31m-=-\033[m'*30)
print(f'A quantidade de vitórias consecutivas foi de: {vitorias}')
print('\033[1;31m-=-\033[m'*30)