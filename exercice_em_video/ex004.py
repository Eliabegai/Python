# informar qual a classificação da palavra é:
t = input('digite algo: ')
print('Tipo primitivo: ', type(t))
print('É Numérico? {0};''\n''É alfabético? {1};''\n''É alphanumérico: {2};''\n''Tem espaço? {3};'
      .format(t.isnumeric(), t.isalpha(), t.isalnum(), t.isspace()),)
print('Está em minúsculo? {0};''\n''Está em maiúsculo: {1};''\n''Está Capitalizada? {2};'
      .format(t.islower(), t.isupper(), t.istitle()))
