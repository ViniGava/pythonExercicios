"""Desenvolva um programa que analise um nome recebido e informe se tem o Silva ou não"""

print('\033[1;31m-=-\033[m'*30)
nome = input('Digite o nome da pessoa: ').strip()
nome = nome.upper()
if 'SILVA' in nome:
    print('Tem "Silva" no nome da pessoa')
else:
    print('Não tem "Silva" no nome da pessoa')
print('\033[1;31m-=-\033[m'*30)
