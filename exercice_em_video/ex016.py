# Criar um programa que leia um número qualquer pelo teclado e mostre a porção inteira. Ex: 6.125=tem a parte inteira 6
from math import trunc
num = float(input('Digite um número qualquer. De preferência com vírgula: '))
print('Você digitou o número {}, seu número inteiro é {}.'.format(num, trunc(num)))
