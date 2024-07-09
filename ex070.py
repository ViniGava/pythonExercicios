"""Crie um programa que leia nome e preço de vários produtos, no final mostre total gasto, qauntos custam mais de
R$1000 e o nome do produto mais barato"""

print('\033[1;31m-=-\033[m' * 30)
print('CARRINHO DE COMPRAS')
print('\033[1;31m-=-\033[m' * 30)

soma = totacima = maisbarato = maisbaratoval = 0

while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    if maisbaratoval == 0:
        maisbarato = nome
        maisbaratoval = preco
    soma += preco

    if preco > 1000:
        totacima += 1

    if preco < maisbaratoval:
        maisbarato = nome
        maisbaratoval = preco

    print('-' * 10)
    while True:
        resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SsNn':
            break
    print('-' * 10)
    if resp == 'S':
        continue
    else:
        break

print(f'--------------- FIM DO PROGRAMA ---------------')
print(f'''O total da compra foi R${soma:.2f}
Temos {totacima} custando mais de R$1000.00
O produto mais barato foi {maisbarato} que custa R${maisbaratoval:.2f}''')

print('\033[1;31m-=-\033[m' * 30)