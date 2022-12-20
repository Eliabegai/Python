# Crie um programa que leia varios números inteiros pelo teclado.
# no final da execução, mostre a media entre todos os valores e qual foi o maior número e o menor valor lido.
# O programa deve perguntar ao usuário se ele quer continuar ou não a digitar os valores;
print('''==================================
        Maior e Menor Valor
==================================''')
num = soma = cont = 0
lista = []
c = 's'
while c != 'n':
    num = int(input('\033[32m   Digite um número: \033[m'))
    lista += [num]
    soma += num
    cont += 1
    c = str(input('\033[34mContinuar? [S/N] \033[m')).strip().lower()[0]
print('Você digitou {} números. O maior é {}, o menor é {}.\n'
      'A média entre todos os valores é {:.2f}'.format(cont, max(lista), min(lista), soma / cont))
