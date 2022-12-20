lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita']
# Tuplas são IMUTÁVEIS!!!!!!!!!
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('===' * 15)
for cont in range(0, len(lanche)):
    print(lanche[cont])
