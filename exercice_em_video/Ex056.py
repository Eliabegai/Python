# Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo; O nome do homem mais velho; Quantas mulheres tem menos de 20 anos
lstnome = []
lstidade = []
lstmulher = []
lsthomem = []
year = 0
velho = []
novo = []
idadev = [0]
for c in range(4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    s = str(input('Qual seu sexo?\n'
                  'Digite ´F´ para Feminino e ´M´ para Masculino: ')).upper()
    lstnome += [nome]
    lstidade += [idade]
    year += idade
    if s == 'F':
        if idade <= 20 and s == 'F':
            novo += [nome]
    if s == 'M' and idade > idade:
        velho = [nome]


print('=' * 50)
print('Média de anos: {}'.format(year / 4))
print('Quantas mulheres tem menos de 20 anos? {}'.format(len(novo)))
print('O homem mais velho é {}'.format(velho))
print(idadev)
