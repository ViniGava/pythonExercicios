"""Aprimorar desafio 093 para aceitar varios jogadores."""

print('\033[1;31m=\033[m' * 40)
print(f'{'Cadastro de Jogadores':^40}')
print('\033[1;31m=\033[m' * 40)

aproveitamento = []
jogador = {}
jogadores = []

while True:
  soma= 0 
  jogador['nome'] = str(input('Nome do Jogador: ')).strip()
  qtdjogos = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
  for c in range(0, qtdjogos):
    dado = (int(input(f'Quantos gols na partida {c+1}? ')))
    aproveitamento.append(dado)
    soma += dado
  jogador['gols'] = aproveitamento[:]
  jogador['total'] = soma
  jogadores.append(jogador.copy())
  aproveitamento.clear()
  resp = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
  if resp == 'n':
    break

print('\033[1;31m=\033[m' * 40)

print(jogadores)

print('\033[1;31m=\033[m' * 40)

print(f'{'CÓD':<5} {'NOME':<12} {'GOLS':<15} {'TOTAL':<15}')
print('\033[1;31m-\033[m' * 40)
cont = 0
for jog in jogadores:
  print(f"{cont:<5} {jog['nome']:<12} {str(jog['gols']):<15} {jog['total']:<15}")
  cont += 1

print('\033[1;31m-\033[m' * 40)

while True:
  opc = int(input('Quer ver o aproveitamento de qual jogador? [999 PARA PARAR] '))
  cont = 0
  if opc == 999:
    break
  if 0 <= opc < len(jogadores):
    print(F'-- LEVANTAMENTO DO JOGADOR: {jogadores[opc]['nome']}')
    for gols in jogadores[opc]['gols']:
      print(f'{'=> Na partida':>18} {cont+1}, {'fez'} {gols} gols')
      cont += 1
    print(f'Foi um total de {jogadores[opc]['total']} gols.')
  else:
    print(f'Nao existe jogador com código {opc}! Tente novamente.')
  print('\033[1;31m-\033[m' * 40)
print('<<< VOLTE SEMPRE >>>')
print('\033[1;31m=\033[m' * 40)