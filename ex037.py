print('\033[1;31m-=-\033[m'*30)
print('PROGRAMA DE CONVERSÃO NÚMERICA')
print('\033[1;31m-=-\033[m'*30)

numero = int(input('Digite o número que deseja converter: '))
print('Digite pra qual base o número deve ser convertido')
op = input('1 = \033[1;31mBINÁRIO\033[m\n2 = \033[1;32mOCTAL\033[m\n3 = \033[1;33mHEXADECIMAL\033[m\n')

if op == '1':
    print('Em binário o {} é representado por {}!'.format(numero, bin(numero).lstrip('0b')))
elif op == '2':
    print('Em octa o número {} é representado por {}!'.format(numero, oct(numero).lstrip('0o')))
elif op == '3':
    print('Em hexadecimal o {} é representado por {}!'.format(numero, hex(numero).lstrip('0x')))
else:
    print('\033[1;31mERRO BASE DE CONVERSÃO NÃO ENCONTRADA\nTENTE NOVAMENTE!!!!\033[m')

print('\033[1;31m-=-\033[m'*30)