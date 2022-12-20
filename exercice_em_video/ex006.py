# Leia um número e mostre seu dobro, triplo e raiz quadrada;
print('Vamos fazer algumas operações!')
n = int(input('Digite um número: '))
print('Você digitou: {},\n o dobro é {};\n o triplo é {};\n e a raiz {:.2f};'.format(n, (n*2), (n*3), (n**(1/2))))
