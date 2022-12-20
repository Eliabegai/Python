# Melhore o desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
# So que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários.
from random import randint
pc = randint(0, 10)
cont = 1
print('''================================ 
      Jogo da Adivinhação
             V2.0
================================''')
num = int(input('Em que número eu pensei? [0 a 10]  '))
while num != pc:
    if num < pc:
        num = int(input('Mais! Tente novamente: '))
    else:
        num = int(input('Menos! Tente novamente: '))
    cont += 1
print('Parabéns! Você digitou {} e eu pensei {} também!'.format(num, pc))
print('Você conseguiu em {} tentativas.'.format(cont))
