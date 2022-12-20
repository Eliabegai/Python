# Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher. So que utilizando agora o 'for'
from time import sleep
from emojis import encode
print('\033[36m==============================================\n'
      '       -=-=-=-=-=- TABUADA -=-=-=-=-=-\n'
      '==============================================\033[m')
n = int(input('\n\033[33mDigite um número para ver sua tabuada:\033[m '))
for c in range(0, 11):
      sleep(0.5)
      print('\033[34m{} x {} = {}\033[m'.format(n, c, n * c))
print(encode('\033[30;42mFIM! :ok:\033[m'))
