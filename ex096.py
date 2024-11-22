"""Faça um programa que tenha uma def chamada area(), que receba as dimensoes de um terreno retangular, e mostre a area do terreno"""

print('\033[1;31m=\033[m' * 40)
print(f'{'Cálculo de Área':^40}')
print('\033[1;31m=\033[m' * 40)

def area(larg, compr):
  area = larg * compr
  print(f'A área de um terreno {larg:.1f}x{compr:.1f} é = {area}m²!')

area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))

print('\033[1;31m=\033[m' * 40)