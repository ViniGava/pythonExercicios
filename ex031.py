"""Desenvolva um programa que calcule o valor da passagem do ônibus tendo em conta que viagem até 200km custa R$0,50
e acima custe R$0,45"""

print('='*50)
print('Cálculo de passagens de ônibus')

dist = int(input('Digite a distância da viagem em Km: '))
if dist <= 200:
    print('O preço da passagem será de R${:.2f}!'.format(dist * 0.50))
else:
    print('O preço da passagem sera de R${:.2f}!'.format(dist * 0.45))
print('\033[1;31m-=-\033[m' * 50)
