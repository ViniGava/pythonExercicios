'''Crie uma matriz 3x3 e preencha com valores lido no teclado, no final mostre com a formataçao correta V2'''

print('\033[1;31m=\033[m' * 40)
print(f'{'MATRIZ 3X3 V2':^40}')
print('\033[1;31m=\033[m' * 40)

matriz = [[],[],[]]
somapar = somaterceira = maiorsegunda = 0

for linha in range(0,3):
  for col in range(0,3):
    dado = int(input(f'Digite um valor para [{linha}, {col}]: '))
    matriz[linha].append(dado)
    if dado % 2 == 0:
      somapar += dado
    if col == 2:
      somaterceira += dado
    if linha == 1:
      if dado > maiorsegunda:
        maiorsegunda = dado

print('\033[1;31m=\033[m' * 40)

for linha in range(0,3):
  for col in range(0,3):
    print(f'[ {matriz[linha][col]} ]',end='')
  print('\n')

print('\033[1;31m=\033[m' * 40)

print(f"""A soma dos valores pares é {somapar}
A soma dos valores da terceira coluna é {somaterceira}
O maior valor da segunda linha é {maiorsegunda}""")

print('\033[1;31m=\033[m' * 40)