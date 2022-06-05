#FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO.
p = float(input('Digite o preço do produto: '))
desc = (p / 100) * 95
print('O produto custa {:.2f} reais, mais com 5% de desconto fica {:.2f} reais.'.format(p, desc))
