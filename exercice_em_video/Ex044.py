# Programa que calcule o valor a ser pago por um produto considerando o seu preço normal, e condição de pagamento
# a vista dinheiro/cheque: 10% de desconto; a vista no cartão: 5% de desconto;
# em até 2x no cartão: preço normal; 3x ou mais no cartão: 20% de juros

from time import sleep

print('\033[7;34m-=\033[m' * 40)
print('\033[7;32mConsiderando um produto \033[1;4mX\033[0;7;32m, informe o valor dele e a forma de pagamento.\033[m'
      '\n\033[7;32mVamos analisar qual melhor propósta para você.\033[m')
print('\033[7;34m-=\033[m' * 40)
v = float(input('\033[35mQual o valor do produto? \033[m'))
c = str(input('\033[1;37mQual a condição de pagamento?'
              '\nDigite 1 para pagamento Avista (Dinheiro/ Cheque);'
              '\nDigite 2 para parcelado cartão;'
              '\n Selecione a OPÇÃO: \033[m'))
if c == '2' and c != '1':
    p = int(input('\033[1;37mQuantidade de parcelas: \033[m'))
elif c != '1' and c != '2':
    print('\033[7;1;37mDesculpe, não consegui entender.\033[m')
if c == '1':
    print('\033[36mAnalisando o valor R${:.2f} \033[m'.format(v))
    sleep(2)
    print('\033[36mCalculando o desconto...\033[m')
    sleep(2)
    print('\033[1;32mO valor com desconto R${:.2f}\033[m'.format(v - (v * 0.1)))
elif c == '2':
    print('\033[36mAnalisando o valor R${:.2f} \033[m'.format(v))
    sleep(2)
    print('\033[36mVerificando a condição de pagamento...\033[m')
    sleep(2)
    if p == 1:
        print('\033[1;33mO número de parcela é {} vezes. O valor será de R${:.2f}\033[m'.format(p, v - (v * 0.05)))
    elif p == 2:
        print('\033[1;33mO número de parcela é {} vezes. O valor da parcela R${:.2f}\033[m'.format(p, v / int(p)))
    elif p >= 3:
        print('\033[1;34mO número de parcela é {} vezes. O valor da parcela R${:.2f}.\n\033[1;31mTotal: R${:.2f}\033[m'
              .format(p, (v + (v * 0.2)) / p, v + (v * 0.2)))
