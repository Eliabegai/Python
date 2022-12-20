# Ler a largura e altura de uma parede em metros, calcular a área e a quantidade de tinta necessária para pinta-la.
# Cada litro de tinta pinta uma área de 2m².
print('Sou seu assistente de pintura, e vim te ajudar a calcular a quantidade necessária de tinta.'
      '\nPara eu poder fazer isso vou precisar de alguns dados da parede como a altura e largura.')
alt = float(input('Informe a altura da parede: '))
lar = float(input('Informe a largura da parede: '))
ar = alt * lar
t = ar / 2
print('A área da parede para pintura é {:.1f}m², com isso vai ser necessário {:.2f} litros de tinta.'.format(ar, t))
