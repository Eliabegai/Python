# Faça um programa que leia um ano qualquer e mostre se é BISSEXTO.
ano = int(input('Que ano nós estamos? '))
print('Vou analisar se é ano bissexto.')
print('*--**--*' * 3)
if ano % 4 == 0:
    if ano % 100 or 400 != 0:
        print('Esse ano é Bissexto')
else:
    print('Esse ano não é Bissexto!')
print('*--**--*' * 3)
