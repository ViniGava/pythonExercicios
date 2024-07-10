"""Crie um programa com uma listagem de produtos e seus respectivos preços, no final mostre os dados em forma
tabular"""

print('\033[1;31m=\033[m' * 41)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('\033[1;31m=\033[m' * 41)

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.3,
            'Livro', 34.9)

for pos, item in enumerate(listagem):
    if pos % 2 == 0:
        print(f'{item:.<30}', end='R$ ')
    else:
        print(f'{item:6.2f}')

print('\033[1;31m=\033[m' * 41)
