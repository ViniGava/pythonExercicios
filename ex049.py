"""Refaça o desafio 009, mostrando a tabuada que um usuário escolher, só que agora usando o laço for"""

print('\033[1;31m-=-\033[m'*30)
print('TABUADA')
print('\033[1;31m-=-\033[m'*30)

num = int(input('Digite o número que gostaria de saber a tabuada: '))
multiplicado = int(input('Digite ate qual número você deseja que o programa mostre a tabuada: '))

for c in range(1, multiplicado + 1):
    print('{:2} X {:2} = {}'.format(num, c, num*c))

print('\033[1;31m-=-\033[m'*30)