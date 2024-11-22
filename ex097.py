"""Desenvolva um programa que estilize a funçao print..."""

print('\033[1;31m=\033[m' * 40)
print(f'{'Print Especial':^40}')
print('\033[1;31m=\033[m' * 40)

def escreva(frase):
  line = len(frase) + 4
  print('~' * line)
  print(f'  {frase}')
  print('~' * line)

escreva(str(input('Mensagem: ')))

print('\033[1;31m=\033[m' * 40)
