"""Desenvolva um programa que recebe um número entre 0 e 9999 e apresente quantas unidade, dezenas, centenas e milhares
tem esse número"""

print('\033[1;31m-=-\033[m'*30)
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
print('\033[1;31m-=-\033[m'*30)
