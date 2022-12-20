print('''================================ 
       Calculo Fatorial
             V1.0
================================\n''')
n = int(input('Insira um valor: '))
m = n
r = 1
while not m == 1:
    r = r * m
    m -= 1
print('{}! = {}'.format(n, r))
