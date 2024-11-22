""""Desenvolva um programa que recebe um conjunto de numeros, jogue em uma funçao, e retorne a quantidade de numeros, e qual o maior deles..."""

print('\033[1;31m=\033[m' * 40)
print(f'{'Desempacotamento':^40}')
print('\033[1;31m=\033[m' * 40)

from time import sleep

def maior(*nums):
  print('\033[1;31m=\033[m' * 40)
  print('Analisando os valores passados...')
  nummaior = 0
  for n in nums:
    sleep(.5)
    print(n, end=' ', flush=True)
    if n > nummaior:
      nummaior = n
  print(f'Foram informados {len(nums)} valores ao todo')
  print(f'O maior valor informado foi {nummaior}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

print('\033[1;31m=\033[m' * 40)
