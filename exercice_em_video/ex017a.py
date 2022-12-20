# Leia o comprimento do cateto oposto, cateto adjacente de um triangulo retângulo e calcule o comprimento da hipotenusa
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa do triangulo retângulo é {:.3f}.'.format(hi))
