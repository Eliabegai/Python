# Desenvolva um programa que leia o comprimento de três retas e diga se elas podem ou não formar um triângulo.
print('-=' * 20)
print('Analisador de Triângulo v1.0')
print('-=' * 20)
a = float(input('Seguimento a: '))
b = float(input('Seguimento b: '))
c = float(input('Seguimento c: '))
if a + b > c and b + c > a and a + c > b:
    print('Com os seguimentos {}cm + {}cm + {}cm PODE formar um triangulo.'.format(a, b, c))
else:
    print('Com os seguimentos {}cm + {}cm + {}cm NÃO PODE formar um triangulo.'.format(a, b, c))
