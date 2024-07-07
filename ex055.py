"""Calcule o peso de 05 pessoas e mostre qual foi o maior e o menor peso lido."""

from sys import maxsize

print('\033[1;31m-=-\033[m' * 30)
print('MAIS LEVE / MAIS PESADO')
print('\033[1;31m-=-\033[m' * 30)

pesomaior = 0
pesomenor = maxsize

for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if peso > pesomaior:
        pesomaior = peso
    elif peso < pesomenor:
        pesomenor = peso

print('O MAIOR peso digitado foi: {:.1f}Kg!\nO MENOR peso digitado foi: {:.1f}Kg!'.format(pesomaior, pesomenor))
print('\033[1;31m-=-\033[m' * 30)
