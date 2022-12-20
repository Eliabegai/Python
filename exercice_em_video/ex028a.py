from random import randint  # Randomizar
from time import sleep  # Comando do 'time', para aguardar um tempo
pc = randint(0, 5)  # Randomizar o número
print('-*-' * 10)
print('Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('-*-' * 10)
num = int(input('Em que número eu pensei? '))   # Tenta adivinhar
print('Processando...')
sleep(2)    # Para dar um tempo entre um comando e outro.
if num == pc:
    print('Parabéns, você conseguiu!')
else:
    print('Tente novamente. Eu pensei em {}, e não no {}.'.format(pc, num))
