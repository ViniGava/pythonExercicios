"""Crie um programa que leia vários números inteiros pelo teclado, o programa so para quando
o usúario digitar 999, no final ele somará todos os valores, e mostrará a quantidade de números
digitados e a soma deles"""

cont = soma = 0

while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} números digitados é: {soma}')