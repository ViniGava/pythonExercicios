"""Desenvolva um programa que recebe um nome e mostra alguma informações sobre ele, tais como nome em maiúsculo,
minúsculo, quantidade de letras sem contas os espaços e quantidade de letras do 1º nome"""

print('\033[1;31m-=-\033[m'*30)
name = input('Digite o nome completo: ')
upper = name.upper()
lower = name.lower()
totletters = len(name.replace(' ', ''))
dividido = name.split()
totlettersfirst = len(dividido[0])
print("""Nome em maiúsculo: {}
Nome em minúsculo: {}
Quantidade de letras totais (sem espaços): {}
Quantidade de letras do primeiro nome: {}""".format(upper, lower, totletters, totlettersfirst))
print('\033[1;31m-=-\033[m'*30)
