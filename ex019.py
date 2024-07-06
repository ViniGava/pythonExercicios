"""Desenvolva um programa que recebe o nome de 4 alunos e escolha aleatoriamente um deles para limpar a lousa"""

import random

print('\033[1;31m-=-\033[m'*30)
a1 = input('Digite o nome do 1º aluno: ')
a2 = input('Digite o nome do 2º aluno: ')
a3 = input('Digite o nome do 3º aluno: ')
a4 = input('Digite o nome do 4º aluno: ')
lista = [a1, a2, a3, a4]
print('o aluno sorteado para apagar a lousa foi {}'.format(random.choice(lista)))
print('\033[1;31m-=-\033[m'*30)
