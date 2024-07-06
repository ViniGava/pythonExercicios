from datetime import date
print('\033[1;31m-=-\033[m'*30)
print('ALISTAMENTO NO EXÉRCITO OBRIGATÓRIO')
print('\033[1;31m-=-\033[m'*30)

anoatual = date.today().year
anonasc = int(input('Digite o ano de seu nascimento: '))
idade = anoatual - anonasc

if idade == 18:
    print('\033[1;32mESTÁ NA HORA DE SE ALISTAR SOLDADO\033[m')
elif idade > 18:
    tempo = idade - 18
    print('\033[1;31mJÁ SE PASSARAM {} ANOS DO TEMPO DE ALISTAMENTO!!!\033[m'.format(tempo))
else:
    tempo = 18 - idade
    if tempo == 1:
        print('\033[1;32mESTÁ QUASE NA HORA SOLDADO, ANO QUE VEM VOCÊ SE ALISTA\033[m')
    else:
        print('\033[1;32mAinda faltam {} anos para você se alistar!!!\033[m'.format(tempo))
print('\033[1;31m-=-\033[m' * 30)