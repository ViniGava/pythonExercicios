"""Desenvolva um programa que leia nome e media de um aluno, guardando a situaçao em um dicionario. No final mostre o conteudo da estrutura na tela. """

print('\033[1;31m=\033[m' * 40)
print(f'{'Boletim':^40}')
print('\033[1;31m=\033[m' * 40)

aluno = {'Nome' : str(input('Nome: ')), 'Media' : float(input('Média: '))}

if aluno['Media'] >= 7:
  aluno['Situaçao'] = 'Aprovado'
elif aluno['Media'] >= 5:
  aluno['Situaçao'] = 'Recuperaçao'
else:
  aluno['Situaçao'] = 'Reprovado'

for k, i in aluno.items():
  print(f'{k} é igual a {i}.')

print('\033[1;31m=\033[m' * 40)