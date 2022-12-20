# Desenvolva uma lógica que leia o peso e altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo
# Abaixo de 18.5: Abaixo do Peso; Entre 18.5 e 25: Peso Ideal; 25 até 30: Sobrepeso;
# 30 até 40: Obesidade; Acima de 40: Obesidade Mórbida
print('-=' * 20)
print('Calculo de IMC v1.0')
print('-=' * 20)
print('Vamos calcular o seu IMC, para isso precisamos de alguns dados.')
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura em centímetro? '))/100
imc = peso / altura ** 2
print('O seu IMC é de {:.2f}m²'.format(peso / altura**2))
if imc < 18.5:
    print('Você está abaixo do Peso.')
elif imc < 25:
    print('Você está com o Peso Ideal.')
elif imc < 30:
    print('Você está com Sobrepeso.')
elif imc <= 40:
    print('Você está com Obesidade.')
elif imc > 40:
    print('Você está com Obesidade Mórbida')
else:
    print('Não consegui calcular.')
