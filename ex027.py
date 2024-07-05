nome = input('Digite o nome da pessoa: ').strip().title()
dividido = nome.split()
nomeinicio = dividido[0]
nomefim = dividido[-1]
print('Nome da pessoa: {}\nPrimeiro nome: {}\nÚltimo nome: {}'.format(nome, nomeinicio, nomefim))