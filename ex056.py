"""Desenvolva um programa que leio o nome, idade e sexo de 04 pessoas, e no final mostre, a média de idade,
o nome do homem mais velho e quantas mulheres tem menos de 20 anos"""

print('\033[1;31m-=-\033[m' * 30)
print('MÉDIA DE IDADE, MAIS VELHO E MULHERES MENORES QUE 20 ANOS')
print('\033[1;31m-=-\033[m' * 30)
soma = 0
menor = 0
idademaior = 0

for c in range(1,5):
    print('\033[1;32m------------------ {} PESSOA ------------------\033[m'.format(c))
    nome = input('Digite o nome da {}ª pessoa: '.format(c)).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Digite o sexo da {}ª pessoa! [M / F]:  '.format(c))).upper().strip()
    soma = soma + idade

    if sexo == 'M':
        sexo = int(2)
    elif sexo == 'F':
        sexo = int(1)
    else:
        print('\033[31mSEXO INVÁLIDO\033[m')
        exit()

    if (sexo == 1) and (idade < 20):
        menor = menor + 1
    if (sexo == 2) and idade > idademaior:
        nomevelho = nome
        idadevelho = idade

plural = 'mulher'
if menor > 1:
    plural = 'mulheres'
elif menor == 0:
    menor = 'Nenhuma'

print('\033[1;31m-=-\033[m' * 30)

print('''A média de idade do grupo é de: {:.0f} anos!!!
O {} é o mais velho do grupo com {} anos!!!
{} {} tem menos de 20 anos!!!'''.format((soma/4), nomevelho, idadevelho, menor, plural))

print('\033[1;31m-=-\033[m' * 30)