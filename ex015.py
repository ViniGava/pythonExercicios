km = float(input('Quantos Km o carro percorreu: '))
diasAlugado = int(input('Quantos dias ele ficou alugado: '))
valorKm = km * 0.15
valorDias = diasAlugado * 60
valorFinal = valorKm + valorDias
print('O carro percorreu {}Km, em {} dias e o valor final do aluguel ficou em R${:.2f}'.format(km, diasAlugado, valorFinal))
