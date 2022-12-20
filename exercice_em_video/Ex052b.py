num = int(input('Digite um número: '))
for c in range(2, num):
    if num % c == 0:
        print('{} Não é um número primo'.format(num))
        break
    else:
        print('{} É um número primo!'.format(num))
        break
print('Fim!')
