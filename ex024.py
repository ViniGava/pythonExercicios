cidade = input('Digite o nome da sua cidade: ').strip()
divisao = cidade.split()
if divisao[0].upper() == 'SANTO':
    print('A sua cidade começa com o nome Santo')
else:
    print('A sua cidade não começa com o nome Santo')
