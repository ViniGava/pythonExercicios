frase = input('Digite uma frase: ').strip().lower()
a = frase.count('a')
a1 = frase.find('a') + 1
a2 = frase.rfind('a') + 1
print('A letra "A" aparece {} vezes!'.format(a))
print('A primeira vez em quem aparece a letra A na frase é na posição {}!'.format(a1))
print('A última vez em que aparece a letra A é na posição {}'.format(a2))