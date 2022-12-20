num = int(input('Digite um número: '))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print('{} não é número primo'.format(num))
            break
        else:
            print('{} é um número primo'.format(num))
            break
else:
    print('{} não é um número primo')
