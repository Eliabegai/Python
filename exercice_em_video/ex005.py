# Faça um programa qe leia um número inteiro e mostre na tela o seu sucessor e antecessor.
# li 8, antes vem 7 e depois vem 9
n = int(input('Digite um número: '))
print('Analisando {}, antes dele vem {}, depois vem {}. Legal né?'.format(n, (n-1), (n+1)))
