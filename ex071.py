"""Crie um programa que simule o funcionamento de um caixa eletronico tendo cédula de 50,20,10 e 1 reais"""

print('\033[1;31m-=-\033[m' * 30)
print('CAIXA ELETRÔNICO')
print('\033[1;31m-=-\033[m' * 30)

notas50 = notas20 = notas10 = notas1 = 0

valor = int(input('Digite o valor a ser sacado: '))
while True:
    while valor >= 50:
        notas50 += 1
        valor -= 50
    while valor >= 20:
        notas20 += 1
        valor -= 20
    while valor >= 10:
        notas10 += 1
        valor -= 10
    while valor >= 1:
        notas1 += 1
        valor -= 1
    if valor == 0:
        break

print('\033[1;31m-=-\033[m' * 30)
print(f'''Cédulas de R$50 = {notas50}
Cédulas de R$20 = {notas20}
Cédulas de R$10 = {notas10}
Cédulas de R$1  = {notas1}''')
print('\033[1;31m-=-\033[m' * 30)
