salario = float(input('Digite o salário do funcionário: '))
salarioat = salario
if salario > 1250.00:
    salarioat = (salario + (salario * 0.10))
    aumento = 10
else:
    salarioat = (salario + (salario * 0.15))
    aumento = 15

print('O salário do funcionário passará de \033[1;31mR${:.2f}\033[m para \033[1;32mR${:.2f}\033[m com o aumento de \033[1;32m{}%\033[m'.format(salario, salarioat, aumento))
