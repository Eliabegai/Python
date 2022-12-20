nome = []       # Salvar os nomes digitados
idade = 0       # Para somar as idades e fazer a média no final
mulher = ['']     # Informar as mulheres que tem menos de 20 anos
homem = ''       # Informar o homem mais velho
idadeM = 0     # Idade do homem mais velho
print('-=' * 30)
for c in range(1, 5):
    n = str(input('{}ª Pessoa, digite seu nome: '.format(c)))
    i = int(input('Digite sua idade: '))
    s = str(input('Informe seu sexo.\n'
                  'Digite ´F´ para Feminino e ´M´ para Masculino: ')).upper()
    nome += [n]     # Alimentar a lista com os nomes
    idade += i    # Alimentar a lista com as idades
    if i < 20 and s == 'F':     # Verificar
        mulher += [n]
    if s == 'M' and i > idadeM:
        homem = n
        idadeM = i
    print('-=' * 30)
m = 0
if mulher == ['']:
    m = 'Não tem nenhuma mulher com menos de 20 Anos'
else:
    m = len(mulher)
'\n'
print('''Conforme as informações acima, segue alguns dados.
A média de idade do grupo é: {} Anos;
Mulheres com menos de 20 Anos: {};
O Homem mais velho do grupo é {} com {} anos;'''.format(idade / 4, m, homem, idadeM))
