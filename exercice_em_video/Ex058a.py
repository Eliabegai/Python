from random import randint
pc = randint(0, 10)
acertou = False
cont = 1
print('''================================ 
      Jogo da Adivinhação
             V2.0
================================''')
while not acertou:
    num = int(input('Em que número eu pensei? [0 a 10]: '))
    if num == pc:
        acertou = True
    else:
        if num < pc:
            print('Mais! Tente novamente...')
        else:
            print('Menos! Tente novamente...')
        cont += 1

print('Parabéns! Você digitou {} e eu pensei {} também!'.format(num, pc))
print('Você conseguiu em {} tentativas.'.format(cont))
