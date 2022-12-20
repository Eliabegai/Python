# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem do ônibus cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.
distancia = float(input('Qual a distância da sua viagem? '))
print('Você irá viajar {}Km, sendo assim:'.format(distancia))
if distancia <= 200:
    print('O valor da passagem será de R${:.2f}!'.format(distancia * 0.50))
else:
    print('O valor da passagem será de R${:.2f}!'.format(distancia * 0.45))
