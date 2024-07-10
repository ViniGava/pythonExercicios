"""Crie uma tupla com várias palavras e diga as vogais de cada palavra"""

print('\033[1;31m=\033[m' * 40)
print(f'{'ÁNALISE DE DADOS EM TUPLA':^40}')
print('\033[1;31m=\033[m' * 40)

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programado', 'futuro')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ',end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
print('')

print('\033[1;31m=\033[m' * 40)
