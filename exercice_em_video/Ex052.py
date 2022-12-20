# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número: '))
mult = 0
for c in range(2, num):
    if num % c == 0:
        mult += 1
if mult == 0:
    print('É primo')
else:
    print('Tem {} múltiplos acima de 2 e abaixo de {}'.format(mult, num))
