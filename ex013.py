"""Desenvolva um programa que efetue um aumento de 15% no salário de um funcionário"""

print('\033[1;31m-=-\033[m'*30)
salario = float(input('Digite o salário do funcionário: R$'))
print('O salário do funcionário passará a ser de R${:.2f} após os 15% de aumento'.format((salario * 0.15) + salario))
print('\033[1;31m-=-\033[m'*30)