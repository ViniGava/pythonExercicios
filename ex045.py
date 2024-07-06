"""Desenvolva um jogo de pedra, papel e tesoura, onde o usuário disputará com o computador"""

from random import randint
from time import sleep

print('\033[1;31m-=-\033[m'*30)
print('PEDRA , PAPEL E TESOURA')
print('VAMOS JOGAR?')
print('\033[1;31m-=-\033[m'*30)

dica = int(input('VOCÊ JÁ SABE JOGAR?\nSIM = [1]\nNÃO = [2]\n'))
if dica == 2:
    print('\033[1;31m-=-\033[m' * 30)
    print('''\033[4;33mREGRAS DO JOGO\033[m
\033[1;32mO COMPUTADOR VAI ESCOLHER UMA AÇÃO (PEDRA, PAPEL OU TESOURA)
E VOCÊ TAMBÉM VAI ESCOLHER UMA PARA ASSIM DETERMINAR UM VENCEDOR
PEDRA GANHA DE TESOURA
PAPEL GANHA DE PEDRA
TESOURA GANHA DE PAPEL\033[m''')
    print('\033[1;31m-=-\033[m' * 30)

jogador = int(input('ESCOLHA UMA\n[1] = PEDRA\n[2] = PAPEL\n[3] = TESOURA\n'))
computador = randint(1, 3)

sleep(1.5)

if jogador == 1:
    escolhausuario = 'PEDRA'
elif jogador == 2:
    escolhausuario = 'PAPEL'
else:
    escolhausuario = 'TESOURA'

if computador == 1:
    escolhacomputador = 'PEDRA'
elif computador == 2:
    escolhacomputador = 'PAPEL'
else:
    escolhacomputador = 'TESOURA'

if jogador == computador:
    print('\033[1;33mEMPATOU, NENHUM DOS DOIS GANHOU!!!\033[m')
elif ((jogador == 1) and (computador == 2)) or (jogador == 2 and (computador == 3) or (jogador == 3) and (computador == 1)):
    print('\033[1;31mHAHAHAHA VOCÊ PERDEU!!\033[m')
else:
    print('\033[1;32mPARABÉNS!!! VOCÊ GANHOU!!!\033[m')

print('O COMPUTADOR ESCOLHEU {} E VOCÊ ESCOLHEU {}'.format(escolhacomputador, escolhausuario))
print('\033[1;31m-=-\033[m' * 30)