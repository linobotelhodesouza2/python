#DESAFIOS
#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR.
d =  float(input('Quanto dinheiro voçê tem na carteira? '))
dol = d / 4.77
print('A quantidade que voçê tem na carteira é R${:.2f} reais, isso da para comprar US${:.2f} em dólares.'.format(d, dol))
