"""Crie um programa onde o úsuario possa digitar quantos números quiser, e coloque-os em uma lista, caso já tenha
o número na lista, não adicione-o, No final será exibido todos os números em ordem crescente"""

print('\033[1;31m=\033[m' * 40)
print(f'{'ORDEM CRESCENTE':^40}')
print('\033[1;31m=\033[m' * 40)

numeros = []

while True:
    while True:
        num = str(input('Digite um valor: ')).strip()
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('Digite um valor válido')
            continue
            
    if num not in numeros:
        print('\033[1;32mValor adicionado com sucesso\033[m')
        numeros.append(num)
    else:
        print('\033[1;31mEsse valor já existe na lista, não irei adicioná-lo\033[m')

    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if r in 'sn':
            break
        else:
            print('Por favor, responda com S ou N.')
    if r == 'n':
        break  

numeros.sort()

print('\033[1;31m=\033[m' * 40)  
print(f'Você digitou os valores {numeros}')
print('\033[1;31m=\033[m' * 40)
