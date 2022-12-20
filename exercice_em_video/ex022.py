# Crie um programa que leia um nome completo e mostre
# com letra maiúscula, minúscula, qtd de letra sem espaço e quantas letras tem o 1º nome.
nome = str(input('Insira seu nome aqui: ')).strip()
print('Analisando seu nome...')
print('Seu nome em letra maíscula: {}'.format(nome.upper()))
print('Seu nome em letra minúscula: {}'.format(nome.lower()))
print('Quantas letras tem seu nome: {}.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))
