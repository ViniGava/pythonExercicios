"""Criar uma lista com quantos números o usuario quiser, e dividir em outras 2 listas pares e impares"""

print('\033[1;31m=\033[m' * 40)
print(f'{'LISTA PAR/IMPAR':^40}')
print('\033[1;31m=\033[m' * 40)

lista = []
listapar = []
listaimpar = []

while True:
    while True:
        num = input('Digite um valor: ')
        if num.isnumeric():
            num = int(num)
            lista.append(num)
            break
        else:
            print('Valor inválido! Digite um número inteiro.')
        
    while True:
        resp = input('Quer continuar? [S/N] ').strip().lower()[0]
        if resp in 'sn':
            break
        else:
            print('Resposta inválida! Digite S para sim ou N para não.')
    if resp == 'n':
        break

for cont, numero in enumerate(lista):
    if numero % 2 == 0:
        listapar.append(lista[cont])
    else:
        listaimpar.append(lista[cont])

print('\033[1;31m=\033[m' * 40)

print(f'''A lista completa é {lista}
A lista de pares é {listapar}
A lista de ímpares é {listaimpar}''')

print('\033[1;31m=\033[m' * 40)
