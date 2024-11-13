"""Recebe uma expressão matemática e informe se a expressão está correta"""

print('\033[1;31m=\033[m' * 40)
print(f'{'EXPRESSÃO MATEMÁTICA':^40}')
print('\033[1;31m=\033[m' * 40)

expressao = [str(input('Digite a expressão: ')).strip()]
lista = []

for expr in expressao:
    for simb in expr:
        if simb == '(':
            lista.append('(')
        elif simb == ')':
            if len(lista) > 0:
                lista.pop()
            else:
                lista.append('(')
                break

if len(lista) == 0:
    print('EXPRESSAO CORRETA')
else:
    print('EXPRESSAO INVALIDA')

print('\033[1;31m=\033[m' * 40)