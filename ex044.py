"""Desenvolva uma programa que informe o desconto ou a taxa de juros que será pago dependendo da sua forma de pagamento"""

print('\033[1;31m-=-\033[m'*30)
print('GERENCIADOR DE PAGAMENTOS')
print('\033[1;31m-=-\033[m'*30)

preco = float(input('Preço do produto: R$'))
pagamento = int(input('Forma de pagamento\n\033[1;32mÀ VISTA / CHEQUE [1]\nÀ VISTA NO CARTÃO [2]\nEm até 2x no cartão [3]\n3x ou mais no cartão [4]\033[m\nOpção desejada: '))

if pagamento == 1:
    precoat = preco - (preco * 0.10)
elif pagamento == 2:
    precoat = preco - (preco * 0.05)
elif pagamento == 3:
    precoat = preco
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(preco/2))
elif pagamento == 4:
    parcelas = int(input('Digite em quantas parcelas: '))
    precoat = preco + (preco * 0.20)
    valorparcelas = precoat / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, valorparcelas))
else:
    precoat = preco
    print('\033[1;31mOPÇÃO INVÁLIDA\033[m')

print('\033[1;32mCom a forma de pagamento escolhida o preço do produto passará de R${:.2f} para R${:.2f}\033[m'.format(preco, precoat))

print('\033[1;31m-=-\033[m'*30)