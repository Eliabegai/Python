# Loja super baratao
# Crie um programa que leia o nome e preço de vários produtos.
# O programa deve perguntar se o usuário vai continuar
# No final mostre:
# a - Qual o total gasto na compra
# b - quantos produtos custam mais de 1000 reais
# c - Qual é o nome do mais barato.
print('''\033[7;34m==================================\033[m
\033[7;34m        LOJA SUPER BARATÃO        \033[m
\033[7;34m==================================\033[m''')
print('\033[33;40mInforme quais os produtos comprado e o valor.\033[m')
total = 0
mais = 0
menos = 0
barato = ''

while True:
    print('\033[40m---\033[m' * 15)
    p = str(input('\033[36mProduto: \033[m'))
    v = float(input('\033[36mValor do produto: R$\033[m'))
    total += v
    if v > 1000:
        mais += 1
    if menos == 0:
        menos = v
        barato = p
    if v < menos:
        menos = v
        barato = p
    c = str(input('\033[36mQuer continuar? [S/N] \033[m')).strip().lower()
    while c not in 'sn':
        c = str(input('\033[36mQuer continuar? [S/N] \033[m')).strip().lower()
    if c == 's':
        print('...')
    else:
        break
print('\033[40m~~\033[m' * 15)
print('\033[1;32mO total gasto foi de R${:.2f}\033[m'.format(total))
if mais == 0:
    print('\033[33mNenhum produto mais de R$1000.00\033[m')
elif mais == 1:
    print('\033[35mSomente 1 produto custou mais de R$1000.00\033[m')
else:
    print(f'\033[36m{mais} Produtos custou mais de R$1000.00\033[m')
print('\033[37mO item mais barato é {} que custa R${:.2f}\033[m'.format(barato, menos))
print('{:-^40}'.format('FIM DO PROGRAMA!'))
