# Leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente do ângulo.
from math import cos, sin, tan, radians
num = float(input('Insira um ângulo: '))
s = sin(radians(num))
c = cos(radians(num))
t = tan(radians(num))
print('Esses são os seno, cosseno e tangente:\n'
      'Seno     {:.2f}\n'
      'Cosseno  {:.2f}\n'
      'Tangente {:.2f}'.format(s, c, t))
