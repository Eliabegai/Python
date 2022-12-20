# Escreva um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar; Se é a hora de se alistar; Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o quanto falta ou que passou do prazo.
from datetime import date
dia = int(input('Data de nascimento\nDia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))
print('Analisando a data de nascimento... {} de {} de {}.'.format(dia, mes, ano))
atual = date.today().year
if atual - ano == 18:
    print('Você tem {} anos.\nEstá na hora de se alistar ao Exército! .'.format(atual - ano))
elif atual - ano < 17:
    print('Você tem {} anos hoje.\nEstá quase na hora de se alistar. Falta {} anos.'.format(atual - ano,
                                                                                            atual - ano - 18))
else:
    print('Você tem {} anos Hoje. Já passou {} anos do alistamento.'.format(atual - ano, atual - ano - 18))
