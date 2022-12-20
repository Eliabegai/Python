# Faça um programa que leia o peso de 5 pessoas e no final mostre qual foi o maior e menor peso lido.
print('===' * 20)
print(' ' * 20, 'Detector de peso')
print('===' * 20)
lst = []
for c in range(1, 6):
    p = float(input('Qual o peso da {}ª pessoa? '.format(c)))
    lst += [p]
print('O MAIOR peso é {}\n'
      'O MENOR peso é {}'.format(max(lst), min(lst)))
