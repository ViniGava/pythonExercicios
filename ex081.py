"""Crie um programa que vai ler vários números e colocar em uma lista. depois mostre: quantos numeros foram
digitados, a lista de valores de forma decrescente, se o valor 5 foi digitado e está ou não na lista"""

print('\033[1;31m=\033[m' * 40)
print(f'{'DADOS DE UMA LISTA':^40}')
print('\033[1;31m=\033[m' * 40)
lista = []
poslista = []
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
lista.sort(reverse=True)
for c,n in enumerate(lista):
    if n == 5:
        poslista.append(c)
print('\033[1;31m=\033[m' * 40)
print(f'Você digitou {len(lista)} valores!')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 foi encontrado na lista nas posições {poslista}')
else:
    print('O valor 5 não foi encontrado na lista.')
print('\033[1;31m=\033[m' * 40)