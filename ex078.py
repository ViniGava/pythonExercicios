"""Faça um programa que leia 5 valores e guarde em uma lista, no final mostre o maior e menor valor digitado, e suas
respectivas posições na lista..."""

print('\033[1;31m=\033[m' * 40)
print(f'{'MAIOR/MENOR COM LISTAS':^40}')
print('\033[1;31m=\033[m' * 40)

valores = []
posmaior = []
posmenor = []

for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    
maior = max(valores)
menor = min(valores)

for c in range(len(valores)):
    if valores[c] == maior:
        posmaior.append(c)
    if valores[c] == menor:
        posmenor.append(c)       

print('\033[1;31m=\033[m' * 40)

print(f'Você digitou os valores {valores}.')
print(f'O MAIOR número digitado foi {maior}, nas posições {posmaior}')
print(f'O MENOR número digitado foi {menor}, nas posições {posmenor}')

print('\033[1;31m=\033[m' * 40)
