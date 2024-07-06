"""Desenvolva um programa que recebe o nome de uma cidade e informe se ela começa com SANTO ou não"""

print('\033[1;31m-=-\033[m'*30)
cidade = input('Digite o nome da sua cidade: ').strip()
divisao = cidade.split()
if divisao[0].upper() == 'SANTO':
    print('A sua cidade começa com o nome Santo')
else:
    print('A sua cidade não começa com o nome Santo')
print('\033[1;31m-=-\033[m'*30)
