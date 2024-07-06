"""Desenvolva um programa que que recebe a largura e altura de uma parede e calcula a quantidade de tinta que gastará
para pintar, tendo em conta que 1l pinta 2m² da parede"""

print('\033[1;31m-=-\033[m'*30)
larg = float(input('Digite a largura da parede em metros: '))
alt = float(input("Digite a altura em metros: "))
print('Á àrea da parede a ser pintada é de {}m², e será necessário {}l de tinta'.format(larg * alt, (larg * alt)/2))
print('\033[1;31m-=-\033[m'*30)
