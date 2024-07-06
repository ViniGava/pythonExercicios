"""Desenvolva um programa que recebe uma frase pelo teclado e informe quantas vezes aparece a letra A, a primeira e a
última posição em que ela aparece na frase"""

print('\033[1;31m-=-\033[m'*30)
frase = input('Digite uma frase: ').strip().lower()
a = frase.count('a')
a1 = frase.find('a') + 1
a2 = frase.rfind('a') + 1
print('A letra "A" aparece {} vezes!'.format(a))
print('A primeira vez em quem aparece a letra A na frase é na posição {}!'.format(a1))
print('A última vez em que aparece a letra A é na posição {}'.format(a2))
print('\033[1;31m-=-\033[m'*30)
