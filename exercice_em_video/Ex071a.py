print('''\033[7;34m==================================\033[m
\033[7;34m        LOJA SUPER BARATÃO        \033[m
\033[7;34m==================================\033[m''')
print('\033[33;40mInforme quais os produtos comprado e o valor.\033[m')
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}.00')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('Obrigado, volte sempre!')