import math

oposto = float(input('Digite o cateto oposto em cm: '))
adj = float(input('Digite o cateto adjacente em cm: '))
print('A hipotenusa é: {:.2f}cm'.format(math.hypot(oposto, adj)))