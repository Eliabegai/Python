# Escreva um programa que leia um número inteiro qualquer e peça ao usuário escolher qual sera a base de conversão:
# -1 para binário; -2 para octal; -3 para hexadecimal
n = int(input('Insira um número: '))
print('Selecione um modo de conversão.\n'
      '1. Para Binário\n'
      '2. Para Octal\n'
      '3. Para Hexadecimal')
s = int(input('Digite aqui: '))
b = format(n, 'b')
o = format(n, 'o')
h = format(n, 'x')
if s == 1:
    print('O número {} em Binário é {}'.format(n, b))
elif s == 2:
    print('O número {} em Octal é {}'.format(n, o))
elif s == 3:
    print('O número {} em Hexadecimal é {}'.format(n, h))
else:
    print('Nenhuma das opções acima foi selecionada.')
