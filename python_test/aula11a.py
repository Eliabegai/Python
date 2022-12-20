# Dando cor ao Python
# Código de escape sequence ANSI para configurar cores em seus programas.
# Utilização do código \033[m com as principais possibilidades.
t1 = teste \033[0;30;41m     # Fundo vermelho, letra branca
t2 = teste \033[4;33;44m    # Fundo azul, letra amarela e sublinhada
t3 = teste \033[1;35;43m    # Fundo amarelo, letra roxa e negrito
t4 = teste \033[30;42m      # Fundo verde, letra branca e estilo padrão
t5 = teste \033[m           # Fundo preto, letra cinza e estilo padrão - default python
t6 = teste \033[7;30m       # Fundo branco, letra preta. Utilizado para inverter

