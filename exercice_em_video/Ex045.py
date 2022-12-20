# Crie um programa que faça o computador jogar Jokenpô com você: pedra, papel e tesoura
from random import choice
from time import sleep
print('-=' * 35)
print('Jokenpô V1.0')
print('-=' * 35)
print('Jokenpô consiste em Pedra, Papel e Tesoura.')
jogador = str(input('Vamos Jogar! Pode escolher: ')).lower()
l = ['pedra', 'papel', 'tesoura']
list = choice(l)
print('JÔ')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!')
if jogador == list:
    print('{}\nEmpate!'.format(list.upper()))
elif jogador == 'pedra' and list == 'papel':
    print('{}\nVocê Perdeu!'.format(list.upper()))
elif jogador == 'pedra' and list == 'tesoura':
    print('{}\nVocê Venceu!'.format(list.upper()))
elif jogador == 'papel' and list == 'pedra':
    print('{}\nVocê Venceu!'.format(list.upper()))
elif jogador == 'papel' and list == 'tesoura':
    print('{}\nVocê Perdeu!'.format(list.upper()))
elif jogador == 'tesoura' and list == 'papel':
    print('{}\nVocê Venceu!'.format(list.upper()))
elif jogador == 'tesoura' and list == 'pedra':
    print('{}\nVocê Perdeu!'.format(list))
else:
    print('Não entendi')
