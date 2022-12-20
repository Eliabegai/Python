from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('======================================\n'
      '              JO KEN PÔ!              \n'
      '                 v1.0\n'
      '======================================')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PÔ!')
print('-=' * 20)
print('\033[32mComputador jogou \033[1m{}\033[m'.format(itens[computador]))
print('\033[34mJogador    jogou \033[1m{}\033[m'.format(itens[jogador]))
print('-=' * 20, '\033[1;35m')
if computador == 0:     # Computador jogou pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Vence!')
    elif jogador == 2:
        print('Computador Vence!')
    else:
        print('Jogada Inválida')
elif computador == 1:   # Computador jogou papel
    if jogador == 0:
        print('Computador Vence!')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Vence!')
    else:
        print('Jogada Inválida')
elif computador == 2:   # Computador jogou tesoura
    if jogador == 0:
        print('Jogador Vence')
    elif jogador == 1:
        print('Computador Vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Inválida')
else:
    print('Não entendi. Tente novamente!')