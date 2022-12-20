# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
# Maioridade = 21 Anos
from datetime import date
print('===' * 12)
print('Análise de Maioridade V1.0')
print('===' * 12)
atual = date.today().year       # Saber o ano base para calculo. O ano do computador.
maior = 0
menor = 0
for c in range(1, 8):       # Verificar quantas pessoas são maiores ou menor de idade
    ano = int(input('Digite seu ano de nascimento {}ª pessoa:'.format(c)))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} Pessoas MAIOR de Idade\n{} Pessoas MENOR de Idade'.format(maior, menor))     # Imprimir o resultado
