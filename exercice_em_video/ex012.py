# leia um preço de algum produto, e mostre o novo preço com 5% de desconto;
p = input('Digite o nome de um produto: ')
v = float(input('Digite o valor do produto: '))
d = float(input('Qual o a porcentagem de desconto aplicada? '))
desc = v - ((d / 100) * v)
print('Vamos ver qual o valor final do {}. O preço inicial é RS{}, com o desconto fica em R${}'.format(p, v, desc))
