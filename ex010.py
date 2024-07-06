print('\033[1;31m-=-\033[m'*30)
real = float(input('Digite quantos reais você tem R$'))
print('Com R${:.2f}, você pode comprar US${:.2f}'.format(real, real/3.27))
print('\033[1;31m-=-\033[m'*30)
