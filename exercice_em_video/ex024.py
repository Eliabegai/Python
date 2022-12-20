# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra 'SANTO'.
nome = str(input('Digite a cidade onde mora aqui: ')).strip()
nome1 = nome.upper()
print('Analisando seu nome: {}\n\n'
      'Ela começa com a palavra SANTO? {}'.format(nome, 'SANTO' in nome1))
print('\nA cidade que você mora tem no total {} letras'.format(len(nome1) - nome1.count(' ')))
