# Converta os graus de Celsius para Fahrenheit e Kelvin.
print('Vamos calcular a temperatura em ºF e K a partir do ºC! Preciso da sua ajuda.')
c = float(input('Qual a temperatura nesse momento? ºC'))
print('Vamos converter para Fahrenheit. Considerando que 1ºC equivale a (*1/180 + 32)Fº, \npode se dizer que '
      '{}ºC = {:.1f}ºF!'.format(c, c*1.8+32))
print('Outra unidade de medida é o Kelvin. Considerando que 1ºC equivale a (+273.15)K, \npode se dizer que '
      '{}ºC = {}K!'.format(c, c+273.15))
