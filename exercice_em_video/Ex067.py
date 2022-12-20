# Faça um programa que mostra a tabuada de vários números, um de cada vez. para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
from time import sleep
from emojis import encode
print('\033[36m==============================================\n'
      '       -=-=-=-=-=- TABUADA -=-=-=-=-=-\n'
      '              -=-=- V3.0 -=-=-\n'
      '==============================================\033[m')
n = int(input('\n\033[33mDigite um número para ver sua tabuada:\033[m '))
cont = 0
while n > 0:
    for c in range(0, 11):
      sleep(0.5)
      print('\033[34m{} x {} = {}\033[m'.format(n, c, n * c))
    n = int(input('\n\033[33mDigite um número para ver sua tabuada:\033[m '))
print(encode('\033[30;42mFIM! :ok:\033[m'))
