"""Crie um programa onde o usuário digite cinco valores, e coloque os em uma lista ordenada sem usar o sort"""

print('\033[1;31m=\033[m' * 40)
print(f'{'LISTA ORDENADA SEM SORT':^40}')
print('\033[1;31m=\033[m' * 40)

lista = []

for contador in range(0,5): 
    while True:
        num = str(input('Digite um valor: ')).strip()
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('Digite um valor válido')
            continue
    if (contador == 0) or (num > max(lista)):
        lista.append(num)
        print('Valor adicionado no final da lista.')
    elif num < min(lista):
        lista.insert(0, num)
        print('Valor adicionado na posição 0.')
    elif lista[0] < num < lista[1]:
        lista.insert(1, num)
        print('Valor adicionado na posição 1')
    elif lista[1] < num < lista[2]:
        lista.insert(2, num)
        print('Valor adicionado na posição 2.')
    elif lista[2] < num < lista[3]:
        lista.insert(3, num)
        print('Valor adicionado na posição 3.')
    elif lista[3] < num < lista[4]:
        lista.insert(4, num)
        print('Valor adicionado na posição 4.')
    
print('\033[1;31m=\033[m' * 40)

print(f'Os valores digitados em ordem foram {lista}')

print('\033[1;31m=\033[m' * 40)
