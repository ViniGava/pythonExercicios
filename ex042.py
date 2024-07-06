print('\033[1;31m-=-\033[m'*30)
print('TIPO DE TRIÂNGULO')
print('\033[1;31m-=-\033[m'*30)

r1 = int(input('Digite o 1º segmento: '))
r2 = int(input('Digite o 2º segmento: '))
r3 = int(input('Digite o 3º segmento: '))

if (r1 + r2 > r3) & (r2 + r3 > r1) & (r1 + r3 > r2):
    if r1 == r2 & r1 == r3:
        print('\033[1;32mOs segmentos {}, {} e {} formaram um TRIÂNGULO EQUILÁTERO!!!\033[m'.format(r1, r2, r3))
    elif (r1 == r2) or (r1 == r3) or (r2 == r3):
        print('\033[1;32mOs segmentos {}, {} e {} formaram um TRIÂNGULO ISÓSCELES!!!\033[m'.format(r1, r2, r3))
    else:
        print('\033[1;32mOs segmentos {}, {} e {} formaram um TRIÂNGULO ESCALENO!!!\033[m'.format(r1, r2, r3))
else:
    print('\033[1;31mOs segmentos {}, {} e {} NÃO PODEM formar um triângulo!!!\033[m'.format(r1, r2, r3))
print('\033[1;31m-=-\033[m'*30)