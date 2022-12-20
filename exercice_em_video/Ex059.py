# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# O programa deve realizar a operação solicitada em cada caso.
from time import sleep
print('''================================ 
        Menu de Opções
             V1.0
================================\n''')
n = 0
n1 = int(input('Insira um número: '))
n2 = int(input('Insira um número: '))
print('-=' * 15)
while not n == 5:
    print('''Menu:
    
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa
    ''')
    opcao = int(input('Selecione uma opção: '))
    n = opcao
    if opcao == 1:
        print('------------')
        print('A soma entre {} + {} = {}'.format(n1, n2, n1 + n2))
        print('Selecione outra opção...')
    elif opcao == 2:
        print('------------')
        print('Multiplicando {} x {} = {}'.format(n1, n2, n1 * n2))
        print('Selecione outra opção...')
    elif opcao == 3:
        print('------------')
        lista = [n1, n2]
        if n1 == n2:
            print('Os dois números são iguais!')
        else:
            print('O maior número é {}'.format(max(lista)))
        print('Selecione outra opção...')
    elif opcao == 4:
        print('------------')
        print('Vamos trocar os números...')
        n1 = int(input('Insira novos números: '))
        n2 = int(input('Insira novos números: '))
        print('Selecione outra opção...')
    elif opcao > 5:
        print('Não entendi, tente novamente!')
    print('-=' * 15)
    sleep(1)
print('Finalizando...')
sleep(2)
print('''================================ 
    Obrigado! Volte Sempre!
================================''')
