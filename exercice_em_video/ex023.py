# Faça um programa que leia de 0 a 9999 e mostre na tela cada um dos digitos separados.
import inspect

n = int(input('Insira um número aqui: '))
print('Analisando o número {} ...'.format(n))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Milhar: {:>2}\n'
      'Centena: {:>1}\n'
      'Dezena: {:>2}\n'
      'Unidade: {:>1}'.format(m, c, d, u))
