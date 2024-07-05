print('='*50)
print('Cálculo de passagens de ônibus')

dist = int(input('Digite a distância da viagem em Km: '))
if dist <= 200:
    print('O preço da passagem será de R${:.2f}!'.format(dist * 0.50))
else:
    print('O preço da passagem sera de R${:.2f}!'.format(dist * 0.45))