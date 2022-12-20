# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça ao usuário tentar descobrir
# qual foi o número escolhido do computador. O programa devera escrever na tela se o usuário venceu ou não.
import random
n = [0, 1, 2, 3, 4, 5]
n1 = random.choice(n)
print('O computador irá escolher um número entre 0 e 5. Tente acertar o número selecionado.')
num = int(input('Digite um número: '))
if num == n1:
    print('Parabéns!!! Você acertou o número {}.'.format(n1))
else:
    print('Tente outra vez!')
