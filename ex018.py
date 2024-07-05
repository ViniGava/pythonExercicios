import math

ang = int(input('Digite o ângulo para saber seu seno, cosseno e tangente: '))
rad = math.radians(ang)
print('Ângulo: {}º\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(ang, math.sin(rad), math.cos(rad), math.tan(rad)))