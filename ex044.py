"""Desenvolva uma programa que informe o desconto ou a taxa de juros que será pago dependendo da sua forma de pagamento"""

print('\033[1;31m-=-\033[m'*30)
print('GERENCIADOR DE PAGAMENTOS')
print('\033[1;31m-=-\033[m'*30)

preco = float(input('Preço do produto: '))
pagamento = int(input('Forma de pagamento\n\033[1;32mÀ VISTA / CHEQUE [1]\nÀ VISTA NO CARTÃO [2]\nEm até 2x no cartão [3]\n3x ou mais no cartão [4]\033[m\n'))

if pagamento == 1:
    precoat = preco - (preco * 0.10)
elif pagamento == 2:
    precoat = preco - (preco * 0.05)
elif pagamento == 3:
    precoat = preco
else:
    precoat = preco + (preco * 0.20)

print('Com a forma de pagamento escolhida o preço do produto ficará R${:.2f}'.format(precoat))

print('\033[1;31m-=-\033[m'*30)