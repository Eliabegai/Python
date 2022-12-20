# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria de acordo com a idade:
from datetime import date
ano = int(input('Que ano você nasceu? '))
atual = date.today().year
idade = atual - ano
print(idade)
if idade <= 9:
    print('Você foi selecionado para a categoria MIRIM! Parabéns.')
elif idade <= 14:
    print('Você foi selecionado para a categoria INFANTIL! Parabéns.')
elif idade <= 19:
    print('Você foi selecionado para a categoria JUNIOR! Parabéns.')
elif idade == 20:
    print('Você foi selecionado para a categoria SÊNIOR! Parabéns.')
elif idade > 20:
    print('Você foi selecionado para a categoria MASTER! Parabéns.')
else:
    print('Não consegui entender...')
