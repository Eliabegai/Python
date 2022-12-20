# Escreva um programa para aprovar um empréstimo bancário de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. Consulte o valor da prestação mensal,
# sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep
color = {'clear': '\033[m',
         'purpleblackbold': '\033[1;35;40m',
         'bluebold': '\033[1;34m',
         'cyanobold': '\033[1;36m',
         'yellowbold': '\033[1;33m',
         'purple': '\033[35m',
         'cyano': '\033[36m',
         'yellow': '\033[33m',
         'greenblackbold': '\033[1;32;40m',
         'green': '\033[32m',
         'redblackbold': '\033[1;31;40m',
         'red': '\033[31m'}
print('{}Para fazer um empréstimo bancário para compra de uma casa.{}'.format(color['purpleblackbold'], color['clear']))
casa = float(input('{}Qual o valor da casa? {}'.format(color['bluebold'], color['clear'])))
sleep(1)
salario = float(input('{}Qual seu salário? {}'.format(color['cyanobold'], color['clear'])))
sleep(1)
ano = float(input('{}Qual o tempo desejado para pagar? Em ano... {}'.format(color['yellowbold'], color['clear'])))
sleep(1)
tempo = ano * 12
parcela = casa / tempo
print('{}Você quer comprar uma casa no valor de R${:.2f}{}'.format(color['purple'], casa, color['clear']))
print('{}Analisando a sua renda...{}'.format(color['cyano'], color['clear']))
sleep(2)
print('{}Considerando {:.1f} meses...{}'.format(color['yellow'], tempo, color['clear']))
sleep(2)
if parcela < salario * 0.3:
    print('{}Aprovado!{}\n{}O valor da parcela mensal será de R${:.2f}{}'
          .format(color['greenblackbold'], color['clear'], color['green'],parcela, color['clear']))
else:
    print('{}Negado!{}\n{}O valor da parcela mensal é de R${:.2f}, sendo maior que 30% da sua renda.{}'
          .format(color['redblackbold'], color['clear'], color['red'], parcela, color['clear']))
