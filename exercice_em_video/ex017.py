# Leia o comprimento do cateto oposto, cateto adjacente de um triangulo retângulo e calcule o comprimento da hipotenusa
from math import pow, sqrt
print('Sabendo que para calcular a hipotenusa utiliza  a fórmula a² + b² = c², onde que c é o lado maior.'
      '\nSabendo disso, vamos calcular! ')
print('Vou pedir para você os valores do cateto adjacente, oposto agora ok?')
co = float(input('Digite qual o comprimento do cateto oposto: '))
ca = float(input('Digite qual o comprimento do cateto adjacente: '))
s = pow(co, 2) + pow(ca, 2)
print('Sabemos que o cateto oposto é de {}, e o adjacente é {}. Vamos calcular a hipotenusa.'
      '\n{}² + {}² = c²'.format(co, ca, co, ca))
print('{} = c²'
      '\nc = √{}'
      '\nc = {:.3f}'.format(s, s, sqrt(s)))
