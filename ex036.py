"""Desenvolva um programa que calcula a prestação de uma casa baseada na quantidade de anos e informe se o empréstimo
será aprovado ou não tendo em base que a prestação não poderá passar de 30% do salário mensal do comprador"""

print('\033[1;31m-=-\033[m'*30)
print('                       Empréstimo Bancário')
print('\033[1;31m-=-\033[m'*30)

valorcasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário mensal: '))
anos = int(input('Digite em quantos anos deseja pagar a casa: '))
prestacao = (valorcasa / (anos * 12))

print('A prestação mensal da casa ficou R${:.2f}'.format(prestacao))

if prestacao > (salario * 0.30):
    print('\033[1;31mO empréstimo foi NEGADO\033[m!!!')
else:
    print('\033[1;32mO empréstimo foi APROVADO\033[m!!!')
print('\033[1;31m-=-\033[m'*30)
