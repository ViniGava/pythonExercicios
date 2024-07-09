"""Programa mostra a tabuada de vários números e só para quando o núm digitado for negativo"""

print('\033[1;31m-=-\033[m'*30)
print('TABUADA')
print('\033[1;31m-=-\033[m'*30)

while True:
    print('\033[1;33m-\033[m' * 41)
    num = int(input('Digite um número para ver sua tabuada: '))
    print('\033[1;33m-\033[m' * 41)
    if num < 0:
        print('Programa Encerrando...\n')
        break
    for c in range(1, 11):
        print(f'{num:2} x {c:2} = {num*c:2}')

print('\033[1;31m-=-\033[m'*30)
print('FIM')
print('\033[1;31m-=-\033[m'*30)