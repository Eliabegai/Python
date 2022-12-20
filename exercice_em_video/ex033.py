# Faça um programa que leia 3 números e mostre qual é o maior e qual o menor.
n1 = int(input('Insira um número qualquer: '))
n2 = int(input('Insira um número qualquer: '))
n3 = int(input('Insira um número qualquer: '))
lista = [n1, n2, n3]
maior = max(lista)
menor = min(lista)
print('Menor Número é {}.'.format(menor))
print('Maior Número é {}.'.format(maior))
