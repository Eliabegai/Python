# Crie um programa que leia o nome de uma pessoa e diga se tem 'SILVA' no nome.
nome = str(input('Qual é o seu nome: ')).strip()
print('Analisando nome...')
print('Seu nome é {}.\n\n'
      'Seu nome tem Silva? {}'.format(nome, 'SILVA' in nome.upper()))
