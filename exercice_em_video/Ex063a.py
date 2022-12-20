print('''==================================
      Sequência de Fibonacci
               V1.0
==================================''')
n = int(input('Digite um número: '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('\n', '~' * 30)
print('O {}º número da sequência de Fibonacci é {}'.format(n, t3))
