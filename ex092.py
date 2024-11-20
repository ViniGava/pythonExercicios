"""Crie um programa que leia nome, ano de nasc, e carteira de trabalho e cadastre-os com idade em um dict, se por acaso a ctps for diferente de 0, o dict receberá também o ano de contrataçao e o salário. Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar..."""

print('\033[1;31m=\033[m' * 40)
print(f'{'Cadastro CTPS':^40}')
print('\033[1;31m=\033[m' * 40)

cadastro = {}

cadastro['nome'] = str(input('Nome: ')).strip()
cadastro['idade'] = 2024 - (int(input('Ano de Nascimento: ')))
cadastro['ctps'] = int(input('Carteira de Trabalho (0 Se nao tiver): '))
if cadastro['ctps'] != 0:
  cadastro['contratacao'] = int(input('Ano de Contrataçao: '))
  cadastro['salario'] = float(input('Salário: '))
  cadastro['aposentadoria'] = ((cadastro['contratacao'] + 35) - 2024) + cadastro['idade']

print('\033[1;31m-\033[m' * 40)

print(cadastro)
for k, v in cadastro.items():
  print(f'{k} tem o valor {v}')

print('\033[1;31m=\033[m' * 40)