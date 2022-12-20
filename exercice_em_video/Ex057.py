# Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' e 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
s = str(input('Qual seu sexo? [F/M] ')).strip().upper()[0]  # remover espaço, maiúsculo e só a primeira letra
p = s
c = 0
while p != 'F' and p != 'M':
    t = str(input('Tente novamente: ')).strip().upper()
    p = t
    c += 1
print('\033[1;32mObrigado!\033[m\nVocê digitou {} vezes errado.'.format(c))
