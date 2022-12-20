# Escreva um programa que leia a velocidade de um carro. Se ultrapassar 80Km/h, mostre que ele foi multado
# A multa custa R$7,00 por cada Km acima do limite.
from random import randint
velocidade = randint(0, 140)
if velocidade > 80:
    print('O limite da via é de 80Km/h. Você passou a {}Km/h.'
          '\nVocê foi multado em R${},00!'.format(velocidade, (velocidade - 80) * 7))
else:
    print('Sua velocidade é de {}Km/h. Está a baixo da velocidade limite. Parabéns!'.format(velocidade))
