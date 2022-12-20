# Faça um programa que leia o nome completo de uma pessoa, mostre em seguida o primeiro e ultimo nome separadamente
# Ex: Ana Maria de Souza; primeiro = Ana ; último = Souza ;
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome é {}.\nAnalisando...'.format(nome))
print('Seu primeiro nome é: {}'.format(nome.split()[0]))
print('Seu último nome é: {}'.format(nome.rsplit()[-1]))
print('Você transferiu para Eliabe Gai R$4368,48 Reais.\nObrigado!!')
