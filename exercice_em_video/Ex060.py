# Faça um programa que leia um número qualquer e mostre seu fatorial - fazer com [for] e [while]
# Ex:5! = 5x4x3x2x1 = 120
print('''================================ 
       Calculo Fatorial
             V1.0
================================\n''')
n = int(input('Insira um valor: '))
resultado = 1
for c in range(1, n+1):
    resultado = resultado * c
print('{}! = {}'.format(n, resultado))
