# Crie um programa que leia a idade, sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer continuar ou não.
# No final mostre:
# a - Quantas pessoas tem 18 anos
# b - Quantos homens foram cadastrados
# c - Quantas mulheres tem menos de 20 anos.
idade18 = 0
homem = 0
mulher = 0
print('''==================================
        CADASTRE UMA PESSOA
==================================''')
while True:
    i = int(input('Insira sua idade: '))
    if i == 18:
        idade18 += 1
    s = str(input('Insira seu sexo: [F/M] ')).strip().upper()[0]
    while s not in 'MF':
        s = str(input('Insira seu sexo: [F/M] ')).strip().upper()[0]
    if s == 'M':
        homem += 1
    if s == 'F' and i < 20:
        mulher += 1
    print('---' * 10, '\nRegistrado!')
    p = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if p == 'N':
        break
print('~~' * 15)
print(f'Tem {idade18} pessoas com menos de 18 anos;\n'
      f'{homem} Homens foram cadastrados;\n'
      f'Tem {mulher} mulheres com menos de 20 anos.')
