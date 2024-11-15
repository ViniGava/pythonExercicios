'''Crie uma matriz 3x3 e preencha com valores lido no teclado, no final mostre com a formataçao correta'''

print('\033[1;31m=\033[m' * 40)
print(f'{'MATRIZ 3X3':^40}')
print('\033[1;31m=\033[m' * 40)

matriz = [[],[],[]]

for cont in range(0,3):
  for c in range(0,3):
    dado = int(input(f'Digite um valor para [{cont}, {c}]: '))
    matriz[cont].append(dado)

print('\033[1;31m=\033[m' * 40)

for cont in range(0,3):
  for c in range(0,3):
    print(f'[ {matriz[cont][c]:^5} ]',end='')
  print()
  

print('\033[1;31m=\033[m' * 40)