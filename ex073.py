"""Coloque a tabela do brasileirão em uma tupla, depois mostre os 5 primeiros, os 4 últimos, em ordem alfabética
e a posição da Chapecoense"""

print('\033[1;31m=\033[m' * 40)
print(f'{'TIMES DO BRASILEIRÃO':^40}')
print('\033[1;31m=\033[m' * 40)

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo',
         'Athetico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO',)

print(f'Lista de times do brasileirão: {times}')
print('\033[1;32m-\033[m' * 275)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('\033[1;32m-\033[m' * 90)
print(f'Os 4 últimos são: {times[-4:]}')
print('\033[1;32m-\033[m' * 68)
print(f'Os times em ordem alfabética fica: {sorted(times)}')
print('\033[1;32m-\033[m' * 279)
print(f'O time da Chapecoense está na {times.index('Chapecoense') + 1}ª posição')

print('\033[1;31m=\033[m' * 40)
