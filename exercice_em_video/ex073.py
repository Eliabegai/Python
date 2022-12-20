# Crie uma tupla preenchida com os 20 primeiros colocado da Tabela do Campeonato Brasileiro de Futebol
# na ordem de colocação. Depois mostre
# a - Apenas os 5 primeiros colocados
# b - Os ultimos 4 colocados da tabela
# c - Uma lista com os times em ordem alfabética
# d - Em que posição na tabela está o time chapecoense.
times = ('Atletico-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
         'Red Bull Bragantino', 'Fluminense', 'America-MG', 'Atletico-GO',
         'Santos', 'Ceara', 'Internacional', 'Sao Paulo', 'Athletico-PR',
         'Cuiaba', 'Juventude', 'Gremio', 'Bahia', 'Sport', 'Chapecoense')
print(f'Os 5 primeiros colocados do Brasileirão: \n{times[0:5]}')
print(f'Os últimos colocado da lista: \n{times[16:20]}')
t = sorted(times)
print(t, end='\n')
