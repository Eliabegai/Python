# Ler um valor em metros e exibir convertido em centímetros e milímitros;
# Kilometro (Km), Hectômetro (hm), Decâmetro (dam), Metro (m), Decímetro (dm), Centímetro (cm), milímetro (mm)
print('Vamos brincar de calcular distância. Você fala em metros e eu mostro em cm e mm.')
m = float(input('Vamos começar então. Qual a distância da sala para o quarto em metros. '))
cm = m *100
mm = m *1000
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print('Agora vamos ver esse valor em todas as unidades de medidas. Vamos lá!! \nVocê digitou que tem {} metros certo?'
      .format(m))
print('Agora segue nas outras unidades de medida: \nMilímetro {}mm;\nCentímetro {:.1f}cm;\nDecímetro {}dm;'
      '\nMetro {}m;\nDecâmetro {}dam;\nHectômetro {:.1f}hm; e\nKilometro {:.2f}km;'.format(mm, cm, dm, m, dam, hm, km))
