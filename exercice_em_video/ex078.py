valores = list()
valmax = []
valmin = []

for c in range(0, 5):
    valores.append(int(input(f'Digite o {c+1}º valor: ')))  # impressão dos valores e salvar na variavel
    print(valores)
    # análise dos valores:
    valmax = max(valores)
    print(valmax)
    valmin = min(valores)
    print(valmin)



print(valores)

print(f'O maior valor é {valmax}')
print(f'O menor valor é {valmin}')







