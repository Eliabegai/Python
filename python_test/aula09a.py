# Manipulação de texto
frase = 'Curso em Vídeo Python'
print(frase[9])  # Nesse caso vai pegar a letra número 9 de frase;
print(frase[9:13])  # Nesse caso pega de 9 a 13, porém o último ele exclui. Último valor não entra na contagem;
print(frase[9:21])
print(frase[9:21:2])  # Nesse caso ele vai do 9 ao 21, porém pulando dois espaço entre si;
print(frase[:5])  # Quando tem essa condição, entende que começa do zero e vai até o 5;
print(frase[15:])  # Indica o início até o final (utilizado quando não sabe o final, por exemplo);
print(frase[9::3])
# Começa no 9 e vai até o final, como entre os 2 pontos considera o final. O 3 é o número de espaços que pula;
# Análise
print(len(frase))  # Conta quantos caracteres tem na frase ou palavra selecionada; Nessa frase tem (0-21)
print(frase.count('o'))  # Conta na frase ou palavra quantos 'o' tem, por exemplo;
print(frase.count('o', 0, 13))  # Considera entre o 0 e 13, e calcula quantos 'o' tem nesse trecho. Obs. O 13 não conta;
print(frase.find('deo'))  # Quantas vezes ele encontrou 'deo', e informa onde começa a frase;
print(frase.find('Android'))  # Quando coloca algo que não existe ou não foi encontrado, retorna o valor de -1;
# pode utilizar o operador 'in' para verificar na frase ou palavra, retornando True ou False;
print('Curso' in frase)
# Transformação
# Uma lista de string é imutável, mas pode modificar através de métodos;
print(frase.replace('Python', 'Android'))   # Utilizado para substituir uma palavra por outra, ou reposicionar;
print(frase.upper())    # Deixa todas as letras em maiúsculo, (as que já estão, permanece);
print(frase.lower())    # Deixa todas as letras em minúsculo, (as que já estão, permanece);
print(frase.capitalize())   # Coloca a primeira letra da frase ou palavra em Maiúsculo, restante em minúsculo;
print(frase.title())    # Coloca o início de frase com letra maiúscula, o restante minúsculo.
frase1 = '   Aprenda Python  '
print(frase1)   # Frase que seria "impressa" normalmente;
print(frase1.strip())   # Em casos que tenha espaços inúteis no começo ou final da frase, use esse comando para limpar;
# Utilizado muito frequente em cadastro de sites, pois pode acontecer de deixar espaço quando for começar a digitar;
print(frase1.rstrip())  # Apaga apenas espaços desnecessários a direita (Right);
# Ao ter o 'r' ou 'l' no começo do método, é relacionado a Right e Left;
print(frase1.lstrip())  # Remove apenas os espaços a esquerda (Left);
# Divisão de string
print(frase.split())    # Na string, verifica onde tem espaço e divide as palavras, Cada palavra tem sua numeração;
# A numeração é reiniciada em cada palavra. Curso é de (0-5), em (0-1), Vídeo (0-4), Python (0-5);
# Estudar melhor como funciona esse comando, será necessário mais adiante!;
print('-'.join(frase))  # Vai juntar todos os elementos de frase (linha 34) e juntar com o elemento de string '-' entre;
# Quando for colocar um texto muito grande para imprimir, pode ser utilizado """ no começo e """ no fim. Exemplo:
print("""Para fazer a prova, é preciso levar:
Documento de identificação original com foto;
Caneta esferográfica azul fabricada em material transparente.
A Fuvest recomenda, ainda, que os candidatos levem máscaras reserva para o caso de necessidade de troca durante a prova.
Também é recomendável levar sua própria garrafa de água já abastecida.
É permitido o uso de lápis (ou lapiseira) para rascunho e de borracha, apontador e régua transparente;""")
