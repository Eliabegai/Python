# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só va parar quando o usuário digitar o valor 999, sendo a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles.
# (Desconsiderando o flag[999])..
print('''==================================
        Tratando Valores
==================================''')
soma = 0 - 999
cont = 0 - 1
n = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    soma += n
    cont += 1
print('Você digitou {} numeros. A soma de todos é {}'.format(cont, soma))
