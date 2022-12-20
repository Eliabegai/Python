# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.
from emojis import encode
soma = 0
for c in range(1, 500):
    if c % 3 == 0:
        print(c)
        soma += c
print('A soma dos números ímpares é: {}'.format(soma))
print(encode('END :floppy_disk:'))
