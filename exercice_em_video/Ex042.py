# Reforço desafio 35, dos triangulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
# Equilátero: todos os lados iguais; Isósceles: dois lados iguais; Escaleno: todos os lados diferentes
print('-=' * 20)
print('Analisador de Triângulo v2.0')
print('-=' * 20)
a = float(input('Seguimento a: '))
b = float(input('Seguimento b: '))
c = float(input('Seguimento c: '))
if a + b > c and b + c > a and a + c > b:
    print('Com os seguimentos {}cm + {}cm + {}cm PODE formar um triângulo.\nTipo do triângulo:'.format(a, b, c))
else:
    print('Com os seguimentos {}cm, {}cm + {}cm NÃO PODE formar um triângulo.'.format(a, b, c)), exit()
if a == b == c:
    print('Triângulo Equilátero')
elif a == b != c or a == c != b or b == c != a:
    print('Triangulo Isóceles')
elif a != b != c:
    print('Triângulo Escaleno')
else:
    print('Triângulo...')