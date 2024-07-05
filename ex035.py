r1 = int(input('Digite o comprimento da 1ª reta: '))
r2 = int(input('Digite o comprimento da 2ª reta: '))
r3 = int(input('Digite o comprimento da 3ª reta: '))

if (r1 + r2 > r3) & (r1 + r3 > r2) & (r2 + r3 > r1):
    print('Com as retas {}cm, {}cm, {}cm é possível formar um triângulo!!!'.format(r1, r2, r3))
else:
    print('Com as retas {}cm, {}cm, {}cm não é possível formar um triângulo!!!'.format(r1, r2, r3))