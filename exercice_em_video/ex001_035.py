color = {'clear': '\033[m',  # Biblioteca de cores
         'blue': '\033[34m',
         'bluebold': '\033[1;34m',
         'backblue': '\033[30;44m',
         'backbluewhite': '\033[44m',
         'blueblacknegative': '\033[7;30;44m',
         'backbluebold': '\033[1;30;44m',
         'backblueboldnegative': '\033[7;30;44m',
         'cyano': '\033[36m',
         'backcyano': '\033[30;46m',
         'cyanobold': '\033[1;36m',
         'backcyanobold': '\033[1;30;46m',
         'purple': '\033[35m',
         'backpurple': '\033[30;45m',
         'purplebold': '\033[1;35m',
         'backpurplewhite': '\033[45m',
         'backpurplebold': '\033[1;30;45m',
         'bold': '\033[1m',
         'underline': '\033[4m',
         'underbold': '\033[1;4m',
         'negative': '\033[7m',
         'red': '\033[31m',
         'redbold': '\033[1;31m',
         'green': '\033[32m',
         'backgreen': '\033[30;42m',
         'backgreenbold': '\033[1;30;42m',
         'backgreenwhite': '\033[42m',
         'greenbold': '\033[1;32m',
         'yellow': '\033[33m',
         'backyellow': '\033[30;43m',
         'backyellowwhite': '\033[43m',
         'yellowbold': '\033[1;33m',
         'grey': '\033[37m',
         'backgrey': '\033[30;47m',
         'backgreywhite': '\033[47m',
         'greybold': '\033[1;37m',
         'purplenegative': '\033[7;30;45m',
         'yellowblacknegative': '\033[7;33;40m',
         'yellowblack': '\033[33;40m',
         'cyanoblack': '\033[36;40m',
         'purpleblack': '\033[35;40m',
         'blueblack': '\033[34;40m',
         'backcyanowhite': '\033[46m',
         'cyanoblacknegative': '\033[7;36;40m',
         'blackgreynegative': '\033[7;30;47m',
         'backrednegative': '\033[7;31;40m',
         'backred': '\033[31;40m',
         'backrednegativebold': '\033[7;1;31;40m',
         'greenblacknegative': '\033[7;32;40m'}
from time import sleep
from pygame import mixer
mixer.init()
mixer.music.load('music_001.mp3')
mixer.music.play()
print('\033[7;30;427m-=\033[m' * 30, '\n')
msg = 'Hello World'  # Ex001
print(color['backblue'], msg, color['clear'], '\n')
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
name = str(input('What`s your \033[4;1mname?\033[m '))     # Ex002
print('Prazer em te conhecer {}{}{}!\n'.format(color['cyano'], name, color['clear']))
print('{}Analisando seu nome...{}'.format(color['cyano'], color['clear']))
sleep(2)
print('{}Seu nome tem Silva? {}{}'.format(color['green'], 'SILVA' in name.upper(), color['clear']))
print('{}Seu primeiro nome é {}{};'.format(color['green'], name.split()[0], color['clear']))
print('{}Seu último nome é {}{};'.format(color['green'], name.rsplit()[-1], color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('Exercício 003, vamos somar!')
n1 = int(input('Insira um \033[34m valor:\033[m '))
n2 = int(input('Insira outro \033[35mvalor:\033[m '))
print('A soma entre {}{}{} e {}{}{} é de {}{}{}.\n'.format(color['bluebold'], n1, color['clear'],
                                                           color['purplebold'], n2, color['clear'],
                                                           color['backpurplebold'], n1 + n2, color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('Análise de palavra. Ex004.')
t = input('{}Digite algo{}: '.format(color['underline'], color['clear']))
print('Tipo {}primitivo?{}    {}{}{}'.format(color['underline'], color['clear'],
                                             color['underbold'], type(t), color['clear']))
print('{}Numérico?{}          {}{}{}'.format(color['red'], color['clear'], color['redbold'],
                                             t.isnumeric(), color['clear']))
print('{}Alfabético?{}        {}{}{}'.format(color['green'], color['clear'], color['greenbold'],
                                             t.isalpha(), color['clear']))
print('{}Alphanumérico?{}     {}{}{}'.format(color['yellow'], color['clear'],
                                             color['yellowbold'], t.isalnum(), color['clear']))
print('Tem {}espaço?{}        {}{}{}'.format(color['blue'], color['clear'], color['bluebold'],
                                             t.isspace(), color['clear']))
print('Está em {}Minúsculo?{} {}{}{}'.format(color['purple'], color['clear'],
                                             color['purplebold'], t.islower(), color['clear']))
print('Está em {}Maiúsculo?{} {}{}{}'.format(color['cyano'], color['clear'],
                                             color['cyanobold'], t.isupper(), color['clear']))
print('Está {}Capitalizada?{} {}{}{}'.format(color['grey'], color['clear'],
                                             color['greybold'], t.istitle(), color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('Ex005 - Ler um número e mostrar o sucessor e antecessor.')
# num = int(input('Digite um número: '))
num = n1
# num = '5'
print('{}Utilizando o mesmo valor do Ex.3{}'.format(color['negative'], color['clear']))
print('O Valor utilizado é {}'.format(num))
print('{}Analisando {}...{}'.format(color['backblueboldnegative'], num, color['clear']))
sleep(1)
print('O {}Antecessor é {}{}\n'
      'O {}Sucessor   é {}{}'.format(color['backbluebold'], num - 1, color['clear'],
                                     color['backcyanobold'], num + 1, color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex006 - Calculando o seu dobro, triplo e raiz quadrada.{}\n'
      '{}Vamos utilizar os mesmos valores do exercício anterior.{}'.format(color['purplenegative'], color['clear'],
                                                                           color['purplenegative'], color['clear']))
num1 = int(num)
from math import sqrt
dob = num1 * 2
tri = num1 * 3
raiz = sqrt(num1)
print('Valor referente {} {} {}.'.format(color['backblue'], num1, color['clear']))
print('{}Dobro: {}{}\n'
      '{}Triplo: {}{}\n'
      '{}Raiz: {:.2f}{}'.format(color['yellowblacknegative'], dob, color['clear'],
                                color['yellowblack'], tri, color['clear'],
                                color['cyanoblacknegative'], raiz, color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex007 - Calculando a média{}'.format(color['cyanoblack'], color['clear']))
print('Utilizando os valores anteriores de {}{}{} e {}{}{},\n'
      'A Média fica em {}{}{};'.format(color['yellowblacknegative'], dob, color['clear'],
                                       color['yellowblack'], tri, color['clear'],
                                       color['purplenegative'], (dob+tri)/2, color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex008 - Convertendo medidas{}'.format(color['backblue'], color['clear']))
print('{}Para: Milímetro, Centímetro, Decímetro, Metro, Decâmetro, Hectômetro e  Kilometro.{}'.format(color['backblue'],
                                                                                                      color['clear']))
print('{}Utilizando o valor do Exercício 3{}'.format(color['backblue'], color['clear']))
num2 = int(num)
print('Convertendo {}{}{} para:\n'
      'Milímetro:  {}{}mm{}\n'
      'Centímetro: {}{}cm{}\n'
      'Decímetro:  {}{}dm{}\n'
      'Metro:      {}{}m{}\n'
      'Decâmetro:  {}{}dam{}\n'
      'Hectômetro: {}{}hm{}\n'
      'Kilometro:  {}{}Km{}'.format(color['backpurplebold'], num2, color['clear'],
                                    color['redbold'], num2 * 1000, color['clear'],
                                    color['greenbold'], num2 * 100, color['clear'],
                                    color['yellowbold'], num2 * 10, color['clear'],
                                    color['bluebold'], num2, color['clear'],
                                    color['purplebold'], num2 / 10, color['clear'],
                                    color['cyanobold'], num2 / 100, color['clear'],
                                    color['greybold'], num2 / 1000, color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex009 - Fazer a tabuada.{}'.format(color['backrednegativebold'], color['clear']))
print('{}Exercício semelhante ao anterior, não necessário refazer.{}'.format(color['backrednegative'], color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex010 - Calcular o valor Real em Dolar.{}'.format(color['purplenegative'], color['clear']))
money = float(input('Qual o valor em {}Real{} que quer converter? R$'.format(color['yellowblacknegative'],
                                                                             color['clear'])))
dolar = float(input('Consulte e informe o valor do {}Dolar{} atualizado: $'.format(color['greenblacknegative'],
                                                                                   color['clear'])))
print('{}Convertendo...{}'.format(color['cyano'], color['clear']))
sleep(2)
print('{}Valor convertido ${:.2f}{}'.format(color['yellowbold'], money / dolar, color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex011 - Calculo de área pintura de uma parede.{}\n'.format(color['backred'], color['clear']))
parede1 = float(input('Informe a altura da parede: '))
parede2 = float(input('Informe o comprimento da parede: '))
paint = (parede1 * parede2) / 2
print('\nTemos as cores {}Azul{}, {}Amarelo{}, {}Verde{}, {}Magenta{}, {}Cyano{} e {}Cinza{} para pintura.\n'
      'Selecione uma delas.\n'.format(color['backbluewhite'], color['clear'],
                                      color['backyellowwhite'], color['clear'],
                                      color['backgreenwhite'], color['clear'],
                                      color['backpurplewhite'], color['clear'],
                                      color['backcyanowhite'], color['clear'],
                                      color['backgreywhite'], color['clear']))
cor = str(input('Qual a cor que deseja? ')).strip().upper()
if cor == 'AZUL':
    ti = color['backblue'] and print('A cor selecionada é {}   {}   {}'.format(color['backblue'], cor, color['clear']))
else:
    if cor == 'AMARELO':
        print('A cor selecionada é {}   {}   {}'.format(color['backyellow'], cor, color['clear']))
    else:
        if cor == 'VERDE':
            print('A cor selecionada é {}   {}   {}'.format(color['backgreen'], cor, color['clear']))
        else:
            if cor == 'MAGENTA':
                print('A cor selecionada é {}   {}   {}'.format(color['backpurple'], cor, color['clear']))
            else:
                if cor == 'CYANO':
                    print('A cor selecionada é {}   {}   {}'.format(color['backcyano'], cor, color['clear']))
                else:
                    if cor == 'CINZA':
                        print('A cor selecionda é {}   {}   {}'.format(color['backgrey'], cor, color['clear']))
                    else:
                        print('{}Desculpe! Não está disponível essa cor.{}'.format(color['redbold'], color['clear']))
print('Area de pintura é {}m², sendo assim necessário {} litros de tinta.\n'
      .format((parede1 * parede2), paint))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex012 - Calculando o preço da tinta com desconto{}'.format(color['yellowblacknegative'], color['clear']))
print('{}Conforme o calculando antes, será necessário {} litros de tinta da cor {}.{}\n'
      '{}O valor aproximado do litro de tinta é de R$15.70.{}\n'.format(color['yellow'], paint, cor, color['clear'],
                                                                        color['yellow'], color['clear']))
if paint <= 10:
    print('O valor da tinta é R${:.2f}'.format(paint * 15.7))
else:
    print('{}O valor da tinta ficou em R${:.2f}{}'.format(color['backgreenbold'], (paint * 15.7) - (paint * 15.7)*0.05,
                                                          color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex013 - Aumento de salário{}'.format(color['backpurplebold'], color['clear']))
salario = float(input('{}Vamos calcular o aumento do seu salário.{}\n'
                      '{}Digite quanto você ganha: R${}'.format(color['purple'], color['clear'],
                                                                color['purple'], color['clear'])))
if salario <= 1250:
    aumento = 15/100
else:
    aumento = 10/100
print('{}Seu antigo salário é R${}0 {}\n'
      '{}Seu novo salário ficou em R${:.2f} {}'.format(color['yellowblack'], salario, color['clear'],
                                                       color['greenblacknegative'], salario + (salario*aumento),
                                                       color['clear']))
print('\n\n{}Exercício 023: {}'.format(color['backpurplewhite'], color['clear']))
print('{}Analisando o número...{}'.format(color['cyano'], color['clear']))
sleep(2)
from math import floor
numb = int(floor(salario))
u = numb // 1 % 10
d = numb // 10 % 10
c = numb // 100 % 10
m = numb // 1000 % 10
print('{}Mostrando o número {} separado.{}'.format(color['blue'], numb, color['clear']))
print('{}Milhar:  {}{};\n'
      '{}Centena: {}{};\n'
      '{}Dezena:  {}{};\n'
      '{}Unidade: {}{};'.format(color['negative'], m, color['clear'],
                                color['negative'], c, color['clear'],
                                color['negative'], d, color['clear'], color['negative'], u, color['clear']))
sleep(2)
print('\n\n{}Ex034 executado junto.{}'.format(color['backgrey'], color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex014 - Converter a temperatura de Celsius para Kelvin e Fahrenheit{}'.format(color['cyanobold'],
                                                                                       color['clear']))
print('Conversor de temperatura')
print('''1. Para converter de ºCelsius para ºFahrenheit
2. Para converter de °Celsius para ºKelvin
3. Para converter ºFahrenheit para ºCelsius''')
cel = float(input('Qual o valor a converter? '))
cel_far = cel * (9/5) + 32
print('O valor convertido é {:.2f}ºF'.format(cel_far))
cel_kel = cel + 273.15
print('O valor convertido é {}ºK'.format(cel_kel))
far_cel = (cel_far - 32) + (5/9)
print('O valor convertido é {:.2f}ºC'.format(far_cel))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex015 - Calculando o aluguel do carro.{}'.format(color['backgreenbold'], color['clear']))
dias = int(input('Quantos {}dias{} utilizou o carro? '.format(color['green'], color['clear'])))
km = float(input('Quantos {}Quilometros{} foi rodado? '.format(color['backyellow'], color['clear'])))
print('Você ficou com o carro {} dias, e andou {}Km. Somando tudo, o valor será de:\n'
      '{}Dias com o carro: R${:.2f}{}\n'
      '{}Quilometros rodados: R${:.2f}{}\n'
      '{}Total da conta: R${:.2f}{}'.format(dias, km, color['greenblacknegative'], dias * 60, color['clear'],
                                            color['yellowblacknegative'], km * 0.15, color['clear'],
                                            color['blueblacknegative'], (dias * 60) + (km * 0.15), color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex016 - Mostrar um número inteiro.{}\n'
      '{}Passar.{}'.format(color['backrednegativebold'], color['clear'], color['backrednegative'], color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex017 - Calcula a Hipotenusa pelo cateto oposto e adjacente{}'.format(color['purplenegative'], color['clear']))
from math import hypot
co = float(input('Comprimento do {}cateto oposto: {}'.format(color['purplebold'], color['clear'])))
ca = float(input('Comprimento do {}cateto adjacente: {}'.format(color['purplebold'], color['clear'])))
hi = hypot(co, ca)
print('A {}Hipotenusa{} do triângulo retângulo é {:.3f}'.format(color['backpurplebold'], color['clear'], hi))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex018 - Mostre o valor de Seno, Cosseno e Tangente de qualquer ângulo.{}'.format(color['backgreywhite'],
                                                                                          color['clear']))
from math import cos, sin, tan, radians
ang = float(input('Insira um ângulo aqui: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('Os valores de\n'
      '{}Seno é {:.2f}{}\n'
      '{}Cosseno é {:.2f}{}\n'
      '{}Tangente é {:.2f}{}'.format(color['cyanoblack'], sen, color['clear'],
                                     color['blueblack'], cos, color['clear'],
                                     color['purpleblack'], tan, color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex019 - Sorteando alguem a relizar uma tarefa. {}'.format(color['backgreywhite'], color['clear']))
import random
pessoa1 = str(input('{}Pessoa 1. Insira um nome:{} '.format(color['blueblack'], color['clear']))).strip()
pessoa2 = str(input('{}Pessoa 2. Insira um nome:{} '.format(color['backblue'], color['clear']))).strip()
pessoa3 = str(input('{}Pessoa 3. Insira um nome:{} '.format(color['yellowblack'], color['clear']))).strip()
pessoa4 = str(input('{}Pessoa 4. Insira um nome:{} '.format(color['backyellow'], color['clear']))).strip()
lista = [pessoa1, pessoa2, pessoa3, pessoa4]
escolhido = random.choice(lista)
print('{}Sorteando...{}'.format(color['greenbold'], color['clear']))
sleep(2)
print('O escolhido foi {} {} {}'.format(color['cyanoblacknegative'], escolhido, color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex020 - Sortear a sequência para o trabalho. {}'.format(color['greenbold'], color['clear']))
print('{}Para simplificar, vamos usar os mesmos escolhidos do exercício anterior. {}'.format(color['green'],
                                                                                             color['clear']))
random.shuffle(lista)
sleep(1)
print('A sequência é...:\n'
      '{} {} {}'.format(color['yellowbold'], lista, color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex021 - Executar uma música.{}'.format(color['green'], color['clear']))
print('{}Executando desde o começo...{}'.format(color['cyano'], color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex022 - Mostre as variações de um nome. {}'.format(color['blue'], color['clear']))
name = str(pessoa1)
separa = name.split()
print('{}Analisando o Nome...{}'.format(color['cyano'], color['clear']))
sleep(2)
print('Seu nome em letra {}Maiúscula{}: {}'.format(color['greenbold'], color['clear'], name.upper()))
print('Seu nome em letra {}Minúscula{}: {}'.format(color['cyanobold'], color['clear'], name.lower()))
print('Seu nome completo tem {}{}{} letras.'.format(color['bluebold'], len(name) - name.count(' '), color['clear']))
print('Seu primeiro é {}{}{} e tem {} {} {} letras.'.format(color['yellowbold'], separa[0], color['clear'],
                                                            color['backyellow'], len(separa[0]), color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex023 - Leia um número e mostre ele separado. {}'.format(color['backpurplewhite'], color['clear']))
print('{}Executado junto no exercício 013.{}'.format(color['blue'], color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex024 - Dizer se a palavra tem `Santo` no nome: {}'.format(color['greenbold'], color['clear']))
city = str(input('{}Qual o nome da sua cidade: {}'.format(color['green'], color['clear']))).upper()
print('{}Analisando a cidade...{}'.format(color['cyano'], color['clear']))
sleep(2)
print('{}A cidade começa com a palavra {}{}Santo?{} {}{}{}'.format(color['blue'], color['clear'], color['bluebold'],
                                                                   color['clear'], color['backbluebold'],
                                                                   'SANTO' in city, color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{} Ex025 - Verificar se o nome tem `Silva`.{}'.format(color['yellowbold'], color['clear']))
print('{}Já feito no início...{}'.format(color['yellow'], color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex026 - Descubra quantas letras `A` tem na frase.{}'.format(color['backrednegative'], color['clear']))
text = str(input('{}Insira um texto ou frase aqui: {}'.format(color['red'], color['clear']))).upper()
print('{}Seu texto tem {} letras.{}'.format(color['blue'], len(text) - text.count(' '), color['clear']))
print('{}Tem {} letras `A`.{}'.format(color['blue'], text.count('A'), color['clear']))
print('{}A letra `A` aparece primeiramente na posição {}.{}'.format(color['cyano'], text.find('A') + 1, color['clear']))
print('{}A letra `A` aparece por último na posição: {}'.format(color['cyano'], text.rfind('A') + 1, color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex027 - Analisando o nome.{}'.format(color['yellowbold'], color['clear']))
print('{}Já feito no início...{}'.format(color['yellow'], color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex028 - Randomizando um número.{}'.format(color['backgreenbold'], color['clear']))
from random import randint
pensar = randint(0, 10)
print('Vou pensar num número de 0(Zero) a 10(Dez), tente adivinhar.')
numero = int(input('Em que número eu pensei? '))
print('{}processando...{}'.format(color['cyano'], color['clear']))
sleep(2)
if numero == pensar:
    print('Parabéns!! Foi esse mesmo que pensei!')
else:
    numero1 = int(input('Tente novamente: '))
    print('{}processando...{}'.format(color['cyano'], color['clear']))
    sleep(2)
    if numero1 == pensar:
        print('Parabéns!! Foi esse mesmo que pensei!')
    else:
        numero2 = int(input('Vamos lá, ultima chance: '))
        print('{}processando...{}'.format(color['cyano'], color['clear']))
        sleep(2)
        if numero2 == pensar:
            print('Parabéns!! Foi esse mesmo que pensei!')
        else:
            print('Que pena, mais sorte na próxima. Eu pensei no número {}.'.format(pensar))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex029 - Radar eletrônico de velocidade.{}'.format(color['blueblack'], color['clear']))
velocidade = randint(0, 140)
if velocidade > 80:
    print('{}O limite de velocidade da via é de 80Km/h.\nVocê passou a {}Km/h.{}\n'
          '{}Sua multa é de R${:.2f}{}.'.format(color['red'], velocidade, color['clear'],
                                                color['redbold'], (velocidade - 80) * 7, color['clear']))
else:
    print('{}Sua velocidade é de {}Km/h. Está dentro do limite de velocidade.{}\n'
          '{}Parabéns!{}'.format(color['green'], velocidade, color['clear'], color['greenbold'], color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('Ex030 - Descobrindo se o número é PAR ou IMPAR.')
numero4 = int(input('Digite um número: '))
if numero4 % 2 == 0:
    print('{}Esse número é PAR!{}'.format(color['blueblacknegative'], color['clear']))
else:
    print('{}Esse número é IMPAR!{}'.format(color['backgreen'], color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('Ex031 - Calculando preço da passagem de ônibus.')
distancia = float(input('Qual a distância da sua viagem? '))
if distancia <= 200:
    print('{}Para a viagem de {}Km, a passagem será de R${:.2f}{}.'.format(color['cyanobold'], distancia,
                                                                           distancia * 0.5, color['clear']))
else:
    print('{}Para a viagem de {}Km, a passagem será de R${:.2f}.{}'.format(color['yellowbold'], distancia,
                                                                           distancia * 0.45, color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex032 - Analisando se o ano é BISSEXTO ou não.{}'.format(color['green'], color['clear']))
ano = int(input('{}Que ano quer analisar? Coloque 0 para analisar o ano atual.\nDigite aqui: {}'
                .format(color['blue'], color['clear'])))
from datetime import date
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}O ano {} é BISSEXTO!{}'.format(color['blue'], ano, color['clear']))
else:
    print('{}O ano {} não é BISSEXTO!{}'.format(color['blue'], ano, color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex033 - Leia 3 números e diga qual o maior e qual o menor.{}'.format(color['backpurplebold'], color['clear']))
from random import randint
n10 = randint(0, 100)
n11 = randint(0, 100)
n12 = randint(0, 100)
print('Os números selecionados são: {}, {}, {};'.format(n10, n11, n12))
print('{}Analisando qual o maior e menor número da lista acima...{}'.format(color['cyano'], color['clear']))
lista = [n10, n11, n12]
print('O {}MAIOR Número{} é: {}{}{}'.format(color['backyellow'], color['clear'],
                                            color['backyellow'], max(lista), color['clear']))
print('O {}MENOR Número{} é: {}{}{}'.format(color['backblue'], color['clear'],
                                            color['backblue'], min(lista), color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex034 - Aumento de salário. Varia conforme você ganha.{}'.format(color['backgreywhite'], color['clear']))
print('{}Executado no exercício 13.{}'.format(color['backgreywhite'], color['clear'],))
print('\033[7;30;47m-=\033[m' * 30, '\n')
sleep(2)
print('{}Ex035 - Leia o comprimento de 3 retas e diga se podem ou não formar um triângulo.{}'
      .format(color['blueblacknegative'], color['clear']))
print('{}Analisador de Triângulo 1.0{}'.format(color['bluebold'], color['clear']))
a = float(input('{}Seguimento a: {}'.format(color['blue'], color['clear'])))
b = float(input('{}Seguimento b: {}'.format(color['green'], color['clear'])))
c = float(input('{}Seguimento c: {}'.format(color['yellow'], color['clear'])))
if a + b > c and b + c > a and a + c > b:
    print('{}Com os seguimentos {}cm, mais {}cm, mais {}cm PODE formar um triângulo.{}'.format(color['cyano'], a, b, c,
                                                                                               color['clear']))
else:
    print('{}Com os seguimentos {}cm, mais {}cm, mais {}cm NÃO PODE formar um triângulo.{}'
          .format(color['cyano'], a, b, c, color['clear']))
print('\033[7;30;47m-=\033[m' * 30, '\n')
