nome = input('nome? ')
print('prazer em te conheçer {:20}!'.format(nome))
print('prazer em te conheçer {:>20}!'.format(nome))
print('prazer em te conheçer {:^20}!'.format(nome))
print('prazer em te conheçer {:=^20}!'.format(nome))
print('\n')
n1 = int(input('Um valor '))
n2 = int(input('Outro valor '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
# print('A soma {}, o produto é {}, a divisão é {:.3f};'.format(s, m, d), end='')
# print('A divisão inteira é {}, a exponenciação é {}'.format(di, e))
print('A soma {},\no produto é {},\na divisão é {:.3f};'.format(s, m, d))
print('A divisão inteira é {},\na exponenciação é {}'.format(di, e))
