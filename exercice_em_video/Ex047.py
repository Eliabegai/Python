# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
from emojis import encode
for c in range(1, 50+1):    # Versão menos otimizada.
    print('.', end='')
    if c % 2 == 0:
        print(encode('{}:grey_exclamation:'.format(c)), end=' ')
print('fim', end='\n')
for n in range(2, 51, 2):       # Versão mais otimizada, onde não repete 2 vezes o mesmo comando
    print('.', end='')
    print(n, end=' ')
