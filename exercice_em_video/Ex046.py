# Faça um programa que mostre uma contagem regressiva na tela para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles; colocar um emoji dos fogos...
from time import sleep
from emojis import encode
for c in range(10, 0, -1):
    sleep(1)
    print('\033[34m {} \033[m'.format(c))
sleep(1)
for c in range(0, 2):
    sleep(0.5)
    print(encode('\033[36m:fireworks::sparkler::sparkles::star2::collision::earth_americas::fireworks::sparkler:'))
