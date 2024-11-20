"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome e quantas partida tem o jogador, depois vai ler a quantidade de gols feitos em cada partida. No final tudo isso será guardado em um dict, incluindo o total de gols feitos durante o campeonato."""

print('\033[1;31m=\033[m' * 40)
print(f'{'Estatisticas do Jogador':^40}')
print('\033[1;31m=\033[m' * 40)

aproveitamento= []
jogador = {}
soma = 0

jogador['nome'] = str(input('Nome do Jogador: ')).strip()
qtdjogos = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for c in range(0, qtdjogos):
  dado = (int(input(f'  » Quantos gols na partida {c+1}? ')))
  aproveitamento.append(dado)
  soma += dado
jogador['gols'] = aproveitamento
jogador['total'] = soma

print('\033[1;31m=\033[m' * 40)

print(jogador)

print('\033[1;31m=\033[m' * 40)

for k, v in jogador.items():
  print(f'O campo {k} tem valor {v}.')

print('\033[1;31m=\033[m' * 40)

print(f'O jogador {jogador['nome']} jogou {qtdjogos} partidas.')
for cont, gols in enumerate(aproveitamento):
  print(f'{'» Na partida':>18} {cont+1}, {'fez'} {gols} gols «')
print(f'Foi um total de {soma} gols.')

print('\033[1;31m=\033[m' * 40)