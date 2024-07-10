"""Criar uma tupla que tenha de 0 a 20 por extenso, e ler pelo teclado um número e represantá-lo por extenso"""

print('\033[1;31m=\033[m' * 40)
print(f'{'NÚMERO POR EXTENSO 0 A 20':^40}')
print('\033[1;31m=\033[m' * 40)

from time import sleep

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

resp = 's'
while resp != 'n':
    num = int(input('Digite um número entre 0 até 20: '))
    while True:
        if num > 20 or num <= -1:
            num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
        else:
            break
    print(f'O número {num} por extenso é {extenso[num]}')
    sleep(1)
    print('\033[1;31m=\033[m' * 40)
    resp = input('Deseja ver outro número? [S/N] ').lower().strip()[0]
    print('\033[1;31m=\033[m' * 40)
