# Faça um programa que jogue par ou ímpar com o computador
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas
# que ele conseguiu no final do jogo;
from random import randint
print('''\033[32m==================================
        Jogo PAR ou ÍMPAR
               V1.0
==================================\033[m''')
win = 0
while True:
    pc = randint(1, 10)
    jog = int(input('Digite um valor:  '))
    while jog > 10:
        jog = int(input('Digite um valor:  '))
    q = str(input('Par ou ímpar? [P/I] ')).strip().lower()[0]
    while q != 'p' and q != 'i':
        q = str(input('Par ou ímpar? [P/I] ')).strip().lower()[0]
    print('===' * 10)
    print(f'Você Jogou {jog}, o computador {pc}')
    print('===' * 10)
    soma = jog + pc
    if q == 'p' and soma % 2 == 0:
        print('Venceu!')
        win += 1
    elif q == 'i' and soma % 2 != 0:
        print('Venceu!')
        win += 1
    else:
        print('Você perdeu!')
        break
print('Fim!')
print(f'Quantidade de vitória: {win}... Parabéns!')
