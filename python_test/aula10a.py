# Condições
# Estruturas condicionais simples e compostas
# comandos ex: carro.siga(), carro.esquerda(), carro.direita(), carro.pare() - Siga, esquerda, direita e pare = método
# Condições são necessárias para poder executar um programa.
# if / else
# representação estruturada
# if carro.esquerda():
#    bloco Left
# else:
#    bloco Right
tempo = int(input('Quantos anos tem seu carro: '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro Velho')
print('--FIM--')
# Condição simplificada
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('--FIM--')
