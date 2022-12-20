# Escreva um programa que leia um número 'n' inteiro qualquer e mostre na tela os 'n' primeiros elementos
# de uma sequência Fibonacci.
# Ex:0 → 1 → 1 → 2 → 3 → 5 → 8...
print('''==================================
      Sequência de Fibonacci
               V1.0
==================================''')
n = int(input('Digite um número: '))
anterior = 0
proximo = 1
cont = 2
total = 0
while cont != n:
    print('{} + {} → {}'.format(anterior, proximo, anterior + proximo),)
    total = proximo + anterior
    anterior = proximo
    proximo = total
    cont += 1
print('O {}º número da sequência Fibonacci é {} '.format(n, total))
