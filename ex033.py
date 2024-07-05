num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
nummaior = num1
nummenor = num1

if num2 > nummaior:
    nummaior = num2
if num3 > nummaior:
    nummaior = num3

if num2 < nummenor:
    nummenor = num2
if num3 < nummenor:
    nummenor = num3

print('Entre {} , {} e {}\nO maior é {}\nO menor é {}'.format(num1, num2, num3, nummaior, nummenor))
