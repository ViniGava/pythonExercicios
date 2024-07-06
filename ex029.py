"""Desenvolva um programa que leia a velocidade de um carro e informe se ela ultrapassou 80km/h, e tendo ultrapassado
calcula o valor da multa tendo em conta que cada km ultrapassado é R$7,00"""

print('\033[1;31m-=-\033[m'*30)
velocidade = int(input('Digite a velocidade do carro: '))

if velocidade > 80:
    print('Você foi multado')
    print('O valor da multa foi de R${:.2f}'.format((velocidade - 80) * 7))
    print('Diminua sua velocidade para ficar em segurança')
else:
    print('Tenha uma boa viagem, continue em segurança!')
print('\033[1;31m-=-\033[m'*30)