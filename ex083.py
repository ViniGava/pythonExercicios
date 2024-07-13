"""Recebe uma expressão matemática e informe se a expressão está correta"""

print('\033[1;31m=\033[m' * 40)
print(f'{'EXPRESSÃO MATEMÁTICA':^40}')
print('\033[1;31m=\033[m' * 40)

expressao = [str(input('Digite a expressão: ')).strip()]
if expressao[0].count('(') == expressao[0].count(')'): 
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

print('\033[1;31m=\033[m' * 40)