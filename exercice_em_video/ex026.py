# Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra 'A'
# em que posição ela aparece a primeira vez e em que posição ela aparece a ultima vez.
text = str(input('Insira um texto ou frase aqui: ')).strip()
print('Seu texto tem {} letras.'.format(len(text)-text.count(' ')))
print('Seu texto tem {} letra A;'.format(text.upper().count('A')))
print('Ela aparece a primeira vez na posição: {}'.format(text.upper().find('A')+1))  # O +1 para nossa contagem
print('Ela aparece na ultima vez na posição: {}'.format(text.upper().rfind('A')+1)) # o +1 para nossa contagem
# Nós contamos, 1,2,3,4,5,6... porém o python começa do zero(0). Para facilitar colocamos o +1 no final.
