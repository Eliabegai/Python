# Sorteie a ordem de apresentação de trabalho dos alunos. Leia o nome dos alunos e mostre a ordem sorteada.
import random
n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação é:\n{}'.format(lista))