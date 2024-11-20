"""Crie um programa que leia o nome de varios alunos e duas notas, no fim mostre o boletim de cada um e permita que o usuario posso ver a nota de cada individualmente."""\

print('\033[1;31m=\033[m' * 60)
print(f'{'BOLETIM ESCOLAR':^60}')
print('\033[1;31m=\033[m' * 60)

dado = []
aluno = []
alunos = []
resp = 's'
cont = 0

while True:
  while resp == 's':
    aluno.append(str(input('Digite o nome do aluno: ')))
    dado.append(float(input('Nota 1: ')))
    dado.append(float(input('Nota 2: ')))
    dado.append((dado[0] + dado[1]) / 2)
    aluno.append(dado[:])
    alunos.append(aluno[:])
    cont += 1
    aluno.clear()
    dado.clear()
    while True:
      resp = str(input('Quer continuar [S/N]: ')).lower().strip()[0]
      if resp in 's,n':
        break
  break

print('\033[1;32m=\033[m' * 60)
print(f'No. {'NOME':^30} {'MÉDIA'}')
print('\033[1;31m-\033[m' * 60)

for j in range(len(alunos)):
  print(f' {j}{alunos[j][0]:^35}{alunos[j][1][2]}')
print('\033[1;31m-\033[m' * 60)

while True:
  resp1 = int(input('Mostrar notas de qual aluno? [999 PARA PARAR]: '))
  if resp1 == 999:
    break
  while resp1 > len(alunos) or resp1 < 0:
    resp1 = int(input('Digite um número válido [999 PARA PARAR]: '))
  print(f'Notas de {alunos[resp1][0]} sao {alunos[resp1][1][0:2]}')
  print('\033[1;31m-\033[m' * 60)

print('''Finalizando Programa...
<<< VOLTE SEMPRE >>>''')

print('\033[1;31m=\033[m' * 60)