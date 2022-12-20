print('''==================================
          Gerador de PA
               V3.0
==================================''')
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a progressão, razão: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += r
        cont += 1
    print('Pausa,')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
