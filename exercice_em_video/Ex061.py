# Refaça o Ex051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
# da progressão usando o while
print('''==================================
          Gerador de PA
               V2.0
==================================''')
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a progressão, razão: '))
termo = p
cont = 1
while cont <= 28:
    print('{}'.format(termo), end='')
    print(' → ' if cont < 10 else '; Fim!', end='')
    termo += r
    cont += 1
