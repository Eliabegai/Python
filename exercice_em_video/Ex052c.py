num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('\n\033[36mO número {} foi dividido {} vezes\033[34m'.format(num, tot))
if tot == 2:
    print('É um número Primo!')
else:
    print('\033[1;31mNÂO\033[0;34m é um número Primo!')
