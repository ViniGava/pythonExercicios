"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando cada uma em um dict, e todos em uma lista, no final mostre qtd de pessoas, lista com todas as mulheres, lista com todos acima da media. """

print('\033[1;31m=\033[m' * 40)
print(f'{'Unindo DICT e LIST':^40}')
print('\033[1;31m=\033[m' * 40)

pessoas = []
pessoa = {}
mulheres = []
soma = 0

while True:
  pessoa['nome'] = str(input('Nome: ')).strip()
  pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().lower()[0]
  while pessoa['sexo'] not in 'mf':
    pessoa['sexo'] = str(input('Digite um Sexo válido [M/F]: '))
  if pessoa['sexo'] == 'f':
    mulheres.append(pessoa['nome'])
  pessoa['idade'] = int(input('Idade: '))
  soma += pessoa['idade']
  pessoas.append(pessoa.copy())
  while True:
    resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resp not in 'sn':
      print('ERRO! Responda apenas com S ou N.')
    else:
      break
  if resp == 'n':
    break
media = soma / len(pessoas)

print('\033[1;31m=\033[m' * 40)

print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {media:5.2f} anos.')
print('- As mulheres cadastradas foram: ',end=' ')
for m in mulheres:
  print(m, end=' ')
print()
print('Lista de pessoas que estao acima da média:')
for p in pessoas:
  if p['idade'] > media:
    print('\n',p)
print('<<ENCERRADO>>')

print('\033[1;31m=\033[m' * 40)