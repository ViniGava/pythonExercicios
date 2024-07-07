"""Faça um programa de uma pessoa, mas só aceite M ou F, caso esteja errado, peça a digitação novamente
até ter um valor correto"""

print('\033[1;31m-=-\033[m' * 30)
print('MASCULINO OU FEMININO')
print('\033[1;31m-=-\033[m' * 30)

r = 1
masc = 0
fem = 0

while r != 0:
    sexo = str(input('Digite o sexo [M/F] [S] para SAIR: ')).lower()
    if sexo == 'm':
        print('\033[1;36mSexo masculino registrado com sucesso\033[m')
        masc += 1
        r = 1
    elif sexo == 'f':
        print('\033[1;35mSexo feminino registrado com sucesso\033[m')
        fem += 1
        r = 1
    elif sexo == 's':
        r = 0
    else:
        r = 1
        print('\033[1;31mSexo inválido, digite de novo\033[m')

print('Você adicionou: \033[36m{} MASCULINOS\033[m\nVocê adicionou: \033[31m{} FEMININOS\033[m'.format(masc, fem))
print('\033[1;31m-=-\033[m' * 30)