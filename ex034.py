salario = float(input('Digite o salário do funcionário: '))
salarioat = salario
if salario > 1250.00:
    salarioat = (salario + (salario * 0.10))
    aumento = 10
else:
    salarioat = (salario + (salario * 0.15))
    aumento = 15

print('O salário do funcionário passará de R${:.2f} para R${:.2f} com o aumento de {}%'.format(salario, salarioat, aumento))
