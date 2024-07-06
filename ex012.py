"""Desenvolva um programa que recebe o preço de um produto e calcule o valor final com um desconto de 5%"""

print('\033[1;31m-=-\033[m'*30)
preco = float(input('Digite o preço do produto: R$'))
print('O valor do produto com desconto de 5% será de R${:.2f}'.format(preco - (preco * 0.05)))
print('\033[1;31m-=-\033[m'*30)