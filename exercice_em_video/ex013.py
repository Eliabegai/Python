# Leia o salário de um funcionário, e mostre o novo salário com 15% de aumento.
s = float(input('Insira seu salário aqui: R$'))
a = float(s + (s * (15 / 100)))
# print('Seu salário = ', a)
print('Seu salário hoje é R${}. Vamos te dar um aumento de 15%, e com isso ele fica em R${:.2f}.'.format(s, a))
