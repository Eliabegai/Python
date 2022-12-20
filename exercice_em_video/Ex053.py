# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços;
# Ex: apos a sopa; a sacada da casa; a torre da derrota; o lobo ama o bolo; anotaram a data da maratona
# palavras que podem ser lidas dos dois lados
print('''========================================
        Detector de Palíndromo.
                 V1.0
========================================''')
w = str(input('Insira uma frase ou palavra: ')).strip().upper()

if w.replace(' ', '') == ''.join(reversed(w.replace(' ', ''))):
    # Esse código é para remover o espaço, deixando apenas as letras
    print('É um palíndromo!')
else:
    print('Não é Palíndromo!! \nEssa essa palavra/ frase ao contrário fica: \n{}'
          .format(''.join(reversed(w.replace(' ', '')))))
