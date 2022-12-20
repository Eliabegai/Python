# Aluguel de carros
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
car = int(input('Quantos dias ficou com o carro? '))
km = float(input('Quantos quilometros foi percorrido? '))
print('Você ficou com o carro {} dias. Cada dia custa R$60,00.\nO total será de R${:.2f};'.format(car, car*60))
print('Você percorreu {}km. Sendo que cada km custa R$0,15. \nO total será de R${:.2f};'.format(km, km*0.15))
print('O total do aluguel do carro é de: \n R${:.2f}!'.format((car*60)+(km*0.15)))
