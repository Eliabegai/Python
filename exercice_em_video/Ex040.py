# Escreva um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final de acordo com a média atingida:
from time import sleep
print('Vamos calcular a média dos alunos.')
nota1 = float(input('Insira a nota 1: '))
nota2 = float(input('Insira a nota 2: '))
media = (nota1 + nota2) / 2
print('\033[36mAnalisando média...\033[m')
sleep(2)
print('\033[34mSua média é {:.1f}\033[m'.format(media))
if media <= 5:
    print('Você \033[1;41mREPROVOU\033[m.\n\033[31mSua média foi abaixo de 5.\033[m')
elif 5 < media < 6.9:
    print('Você está em \033[1;43mRECUPERAÇÃO\033[m.\n\033[33mSua média está em 5 e 7.\033[m')
elif media >= 7:
    print('\033[1;42mParabéns!! Você foi aprovado.\033[m')
else:
    print('Não consegui calcular.')
