"""Desenvolva um programa que recebe um texto do teclado, e apresente alguma informações sobre esse texto"""

print('\033[1;31m-=-\033[m'*20)
algo = input('Digite algo: ')

print('\033[32mO tipo primitivo desse valor é {}\033[m'.format(type(algo)))
print('\033[31mSó tem espaços? {}\033[m'.format(algo.isspace()))
print('\033[32mÉ um número? {}\033[m'.format(algo.isnumeric()))
print('\033[31mÉ alfabético? {}\033[m'.format(algo.isalpha()))
print('\033[32mÉ alfanumérico? {}\033[m'.format(algo.isalnum()))
print('\033[31mEstá em MAIÚSCULAS? {}\033[m'.format(algo.isupper()))
print('\033[32mEstá em minúsculas? {}\033[m'.format(algo.islower()))
print('\033[31mEstá capitalizada? {}\033[m'.format(algo.istitle()))
print('\033[1;31m-=-\033[m'*20)
