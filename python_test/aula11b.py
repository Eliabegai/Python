print('\033[0;;40m Hello World!\033[m')
a = 32
b = 31
print('Os números são \033[32;40m{}\033[m e \033[31;40m{}\033[m.'.format(a, b))
nome = 'Eliabe'
print('Olá, muito prazer em te conhecer {}{}{}!!!'.format('\033[4;32m', nome, '\033[m'))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'pretoebranco': '\033[7m'}
print('Prazer em te conhecer {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
