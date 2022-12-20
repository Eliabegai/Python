s = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Tente novamente: [M/F] ')).strip().upper()[0]
print('Registrado!')
