"""Desenvolva um programa quer leia nome e  peso de varias pessoas guardando em uma lista
no final mostre, a) quantas pessoas foram cadastradas, b) uma listagem com as pessoas mais pesadas,
c)uma listagem com as mais leves..."""

print('\033[1;31m=\033[m' * 40)
print(f'{'LISTAS PESSOAS E PESO':^40}')
print('\033[1;31m=\033[m' * 40)


pessoas = []
pesomaior = []
pesomenor = []
dado = []
resp = 's'
qtd = 0
pesomaiornum = pesomenornum = 0

while resp == 's':
  dado.append(str(input('Nome: ')))
  dado.append(float(input('Peso: ')))
  pessoas.append(dado[:])
  if qtd == 0:
    pesomaiornum = pesomenornum = dado[1]
  if dado[1] < pesomenornum:
    pesomenor.clear()
    pesomenornum = dado[1]
    pesomenor.append(dado[0])
  elif dado[1] > pesomaiornum:
    pesomaior.clear()
    pesomaiornum = dado[1]
    pesomaior.append(dado[0])
  elif dado[1] == pesomaiornum:
    pesomaior.append(dado[0])
  if dado[1] == pesomenornum:
    pesomenor.append(dado[0])
  dado.clear()
  qtd += 1
  while True:
    resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resp in 's,n':
      break

print(f'Ao todo voce cadastrou {qtd} pessoas.')
print(f'O maior peso foi de {pesomaiornum}Kg. Peso de ', end='')
for j in range(len(pesomaior)):
  print(f'[{pesomaior[j]}] ', end='')
print(f'\nO menor peso foi de {pesomenornum}Kg. Peso de ', end='')
for j in range(len(pesomenor)):
  print(f'[{pesomenor[j]}] ', end='')
print('')

print('\033[1;31m=\033[m' * 40)