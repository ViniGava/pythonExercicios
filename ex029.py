velocidade = int(input('Digite a velocidade do carro: '))

if velocidade > 80:
    print('Você foi multado')
    print('O valor da multa foi de R${:.2f}'.format((velocidade - 80) * 7))
    print('Diminua sua velocidade para ficar em segurança')
else:
    print('Tenha uma boa viagem, continue em segurança!')
