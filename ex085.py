"""Receba 7 valores, cadastre em uma lista, depois mostre os impares e pares separadamente em ordem 
crescente"""

print('\033[1;31m=\033[m' * 40)
print(f'{'PARES E IMPARES':^40}')
print('\033[1;31m=\033[m' * 40)

numeros = [[],[]]

for cont in range(0,7):
  dado = int(input(f'Digite o {cont+1}o. valor: '))
  if dado % 2 == 0:
    numeros[0].append(dado)
  else:
    numeros[1].append(dado)

numeros[0].sort()
numeros[1].sort()

print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')




print('\033[1;31m=\033[m' * 40)