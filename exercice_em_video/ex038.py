# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
# O primeiro valor é maior; segundo valor é maior; Não existe valor maior, os dois são iguais
n1 = int(input('Digite um número qualquer: '))
n2 = int(input('Digite um número qualquer: '))
if n1 > n2:
    print('O primeiro valor, {}, é maior que o segundo {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor, {}, é o maior que o primeiro {}'.format(n2, n1))
else:
    print('Os dois números são iguais.')
