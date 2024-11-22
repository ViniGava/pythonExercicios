"""Desenvolva um programa que tenha function contador(), que receba 3 param, inicio, fim e passo e realize a contagem."""

print('\033[1;31m=\033[m' * 40)
print(f'{'Contador':^40}')
print('\033[1;31m=\033[m' * 40)

from time import sleep

def contador(inicio, fim, passo):
  print('=' * 50)
  if passo < 0:
    passo *= -1
  elif passo == 0:
    passo = 1
  print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

  if fim < inicio:
    passo *= -1
    fim -= 1
  else:
    fim += 1
  
  for cont in range(inicio, fim, passo):
    sleep(.5)
    print(cont, end=' ', flush=True)
  print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('=' * 50)
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Ínicio: ')), int(input('Fim: ')), int(input('Passo: ')))


print('\033[1;31m=\033[m' * 40)