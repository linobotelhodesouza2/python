#DESAFIO EXTRA
#ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO E A QUANTIDADE DE DIAS PELOS
# QUAIS ELE FOI ALUGADO.CALCULE O PRECO A PAGAR, SABENDO QUE O CARRO CUSTA R$ 60 REAIS POR DIA E R$0,15 POR
# KM RODADO.

d = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pg = (d * 60) + (km * 0.15)
#pg = km * 0.81667 *** descobri o valor sem ver o video
print('Voçê alugou o carro por {} dias e rodou {} Km, o valor a pagar é de R${:.2f}.' .format(d, km, pg ))

