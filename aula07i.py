#DESAFIOS
#FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO.
p = float(input('Digite o preço do produto R$ '))
desc = (p / 100) * 95 #preco final ,***** forma que eu pensei mais simples *****
#desc = p - (p * 5 / 100) #forma que eu nao tinha pensado
#desc = p * 5 / 100 desconto
print('O produto custa {:.2f} reais, mais com 5% de desconto fica {:.2f} reais.'.format(p, desc))
