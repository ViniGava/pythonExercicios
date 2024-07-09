"""Leia o nome e idade de várias pessoas, no final mostre quantas pessoas tem mais de 18 anos, quantos homens
cadastrados, quantas mulheres menos de 20 anos"""

idadetot = idademtot = homens = 0
continuar = 'S'
while True:
    if continuar == 'N':
        break
    print('\033[1;31m-=-\033[m' * 10)
    print('Cadastre uma pessoa')
    print('\033[1;31m-=-\033[m' * 10)

    idade = int(input('Idade: '))
    while True:
        sexo = input('Sexo [M/F] : ').strip().upper()[0]
        if (sexo == 'F') or (sexo == 'M'):
            break


    if idade >= 18:
        idadetot += 1

    if sexo in 'Mm':
        homens += 1

    if sexo in 'Ff' and idade < 20:
        idademtot += 1

    print('-' * 15)
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if continuar == 'N':
            break
        if continuar == 'S':
            break


print('====== FIM DO PROGRAMA ======')
print(f'''Total de pessoas com mais de 18 anos: {idadetot}.
Ao todo temos {homens} homens cadastrados.
E temos {idademtot} mulheres com menos de 20 anos.''')


print('\033[1;31m-=-\033[m' * 30)
