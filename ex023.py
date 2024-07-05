num = input('Digite um número inteiro entre 0 e 9999: ')
numinv =  num[::-1] + '0000'
unidade = numinv[0]
dezena = numinv[1]
centena = numinv[2]
milhar = numinv[3]
print("""Número digitado: {}
Unidade: {}
Dezena: {}
Centena {}
Milhar {}""".format(numinv, unidade, dezena, centena, milhar))
