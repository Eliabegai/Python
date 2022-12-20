# Escreva um programa que pergunte o salário de funcionário e calcule o valor do seu aumento.
# Para salários superior a R$1250,00, calcule o aumento de 10%. Para os inferiores ou iguais o aumento é de 15%.
salario = float(input('Qual o seu salário? R$'))
if salario >= 1250:
    print('Você recebeu um aumento de 10%. Parabéns!\n'
          'Seu novo salário será de R${:.2f}'.format(salario + (salario*0.1)))
else:
    print('Você recebeu um aumento de 15%. Parabéns!\n'
          'Seu novo salário será de R${:.2f}'.format(salario + (salario*0.15)))
