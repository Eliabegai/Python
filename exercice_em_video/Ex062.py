# Melhore o Ex61, perguntando ao usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.
print('''==================================
          Gerador de PA
               V3.0
==================================''')
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a progressão, razão: '))
quantidade = int(input('Quantos termos quer mostrar: '))
termo = p
cont = quantidade
soma = 0
while not cont == 0:
    print('{}'.format(termo), end='')
    print(' → ' if cont > 1 else '; Fim!', end='')
    termo += r
    cont -= 1
    if cont == 0:
        q = int(input('\nMostrar mais termos: [zero para encerrar]'))
        cont = q
    soma += 1
print('{} termos'.format(soma))
