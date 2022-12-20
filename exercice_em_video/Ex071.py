# Simulador da caixa
# Crie um programa que simule o funcionamento de um caixa eletronico.
# No início, pergunte ao usuário qual será o valor a ser sacado (núm. inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues
#
# Obs.: Considere que o caixa possue cédula de 50, 20, 10 e 1;
print('''\033[7;36m==================================\033[m
\033[7;36m         CAIXA ELETRÔNICO         \033[m
\033[7;36m==================================\033[m''')
valor = int(input('Que valor você quer sacar? R$'))
resto = valor
while resto != 0:
    if resto // 50:
        print('Total de {} notas de R$50.00'.format(resto // 50))
        resto %= 50
    if resto // 20:
        print('Total de {} notas de R$20.00'.format(resto // 20))
        resto %= 20
    if resto // 10:
        print('Total de {} notas de R$10.00'.format(resto // 10))
        resto %= 10
    if resto // 1:
        print('Total de {} notas de R$1.00'.format(resto // 1))
        resto %= 1
print('Volte sempre!')
