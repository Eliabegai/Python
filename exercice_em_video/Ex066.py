# Crie um programa que leia varios números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada
# No final, mostre quantos números foram digitados e qual foi a soma entre eles. (Desconsidere o flag)
print('''==================================
        Tratando Valores
                V2.0
==================================''')
n = soma = cont = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números. A soma de todos é {}'.format(cont, soma))
