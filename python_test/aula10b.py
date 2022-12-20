nome = str(input('Qual é seu nome: '))
if nome == 'Eliabe':
    print('Que nome lindo você tem!')
else:
    print('Nomezinho OK...')
print('Bom dia, {}!'.format(nome))

print('---FIM---')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}.'.format(m))
if m >= 6:
    print('Parabéns, sua média foi boa!')
else:
    print('É uma pena, estude mais na próxima vez!')
print('Parabéns, sua média foi boa!' if m <= 6 else 'É uma pena, estude mais na próxima!')
