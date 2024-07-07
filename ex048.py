"""Faça um programe que calcule todos a soma de todos os números ímpares que são múltiplos de 3 e que se encontram no
intervalo de 1 até 500"""

print('\033[1;31m-=-\033[m'*30)
print('SOMA ÍMPARES, MÚLTIPLOS DE 3\nENTRE 1 E 500')
print('\033[1;31m-=-\033[m'*30)
soma = 0
numq = 0

for c in range(1, 501 , 2):
    if c % 3 == 0:
        soma += c
        numq += 1
print('A quantidade de números ÍMPARES MÚLTIPLOS de 3, entre 01 e 500 são de: \033[1;32m{}\033[m números\nA soma de todos eles é: \033[1;32m{}\033[m'.format(numq, soma))
print('\033[1;31m-=-\033[m'*30)
