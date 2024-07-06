"""Desenvolva um programa que calcule o preço a pagar de um aluguel de carro, baseado na quilometragem rodado
e quantos dias ficou alugado"""

print('\033[1;31m-=-\033[m'*30)
km = float(input('Quantos Km o carro percorreu: '))
diasAlugado = int(input('Quantos dias ele ficou alugado: '))
valorKm = km * 0.15
valorDias = diasAlugado * 60
valorFinal = valorKm + valorDias
print('O carro percorreu {}Km, em {} dias e o valor final do aluguel ficou em R${:.2f}'.format(km, diasAlugado, valorFinal))
print('\033[1;31m-=-\033[m'*30)
