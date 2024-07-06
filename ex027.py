"""Desenvolva um programa que recebe o nome de uma pessoa, e informe o primeiro e último nome independente da quantidade
de nomes"""

print('\033[1;31m-=-\033[m'*30)
nome = input('Digite o nome da pessoa: ').strip().title()
dividido = nome.split()
nomeinicio = dividido[0]
nomefim = dividido[-1]
print('Nome da pessoa: {}\nPrimeiro nome: {}\nÚltimo nome: {}'.format(nome, nomeinicio, nomefim))
print('\033[1;31m-=-\033[m'*30)
