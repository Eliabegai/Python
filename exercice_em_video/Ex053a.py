frase = str(input('Digite uma frase: ')).strip().upper()
p = frase.split()       # Separar as palavras
junto = ''.join(p)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo!')
