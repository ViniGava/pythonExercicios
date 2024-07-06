"""Desenvolva um programa que recebe um valor em metros e informa em outras distâncias aquele mesmo valor"""

print('\033[1;31m-=-\033[m'*30)
m = float(input('Digite um valor em metros: '))
print('\033[1;32mValor em quilômetro: {}km\033[m \n\033[1;31mValor em hectômetro: {}hm\033[m \n\033[1;32mValor em decâmetro: {}dam\033[m'.format((m/1000), (m/100), (m/10)))
print('\033[1;31mValor em metros: {}m\033[m \n\033[1;32mValor em decímetro: {}dm\033[m \n\033[1;31mValor em centímetro: {}cm\033[m \n\033[1;32mValor em milímetro: {}mm\033[m'.format(m, (m*10), (m*100), (m*1000)))
print('\033[1;31m-=-\033[m'*30)
