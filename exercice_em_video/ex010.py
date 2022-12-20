# Mostrar quanto dinheiro a pessoa tem na carteira, e com isso quantos dolar pode adquirir.
print('O mundo hoje, a nossa moeda está muito volátil. Com isso a melhor maneira de guardar um pouco de dinheiro é'
      ' com dolar. Vamos fazer um experimento.')
m = float(input('Quantos reais você tem na sua carteira hoje? R$'))
print('Considerando que o dolar hoje está R$5,61, você tem: ${:.2f} dolares.\natualizado dia 10/12/21.'.format(m / 5.61))
