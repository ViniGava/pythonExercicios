name = input('Digite o nome completo: ')
upper = name.upper()
lower = name.lower()
totletters = len(name.replace(' ', ''))
dividido = name.split()
totlettersfirst = len(dividido[0])
print("""Nome em maiúsculo: {}
Nome em minúsculo: {}
Quantidade de letras totais (sem espaços): {}
Quantidade de letras do primeiro nome: {}""".format(upper, lower, totletters, totlettersfirst))
