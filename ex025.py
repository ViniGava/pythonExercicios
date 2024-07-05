nome = input('Digite o nome da pessoa: ').strip()
nome = nome.upper()
#print('SILVA' in nome)
if 'SILVA' in nome:
    print('Tem "Silva" no nome da pessoa')
else:
    print('Não tem "Silva" no nome da pessoa')
