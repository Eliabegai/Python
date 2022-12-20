# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
from time import sleep
numero = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']
'''num = int(input('Digite um número entre 0 e 20: '))
n = str(num).isnumeric()
print(n)'''
c = 's'
while c == 's':
    num = input('Digite um número entre 0 e 20: ')
    if int(num.isnumeric()):    # Saber se o valor digitado é um número ou não;
        n = int(num)        # Transformando a variável 'num' em um número inteiro;
        if n <= 20:
            if n in range(0, 21):
                print(f'O número que você digitou é \033[30;46m{n}\033[m que por extenso fica '
                      f'\033[30;46m{numero[n].upper()}\033[m')
                c = str(input('Deseja continuar? [S/N] '))
            else:
                print(f'O valor {n} é inválido')
        else:
            print('Inválido! Tente novamente...')
    else:
        print('Inválido! Tente novamente...')
print('Encerrando...')
sleep(2)
print('Fim!')
