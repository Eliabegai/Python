# Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética).
# No final mostre os 10 primeiros termos dessa progressão
p = int(input('Digite o primeiro termo: '))     # primeiro termo
r = int(input('Digite a progressão: '))     # a razão
n = int(input('Quantos elementos exibir: '))    # quantidade de elementos a exibir
u = p + (n-1)*r  # calculando o máximo - 10° termo nesse caso
u = u + 1
for c in range(p, u, r):
    print(c)
print(u)
