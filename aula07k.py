#DESAFIO EXTRA
#CRIE UM PROGRAMA QUE LEIA O PRECO DO PRODUTO E CALCULE SEU VALOR DE PAGAMENTO A VISTA COM DESCONTO DE 15% E
#AUMENTO DE 22% SE FOR PARCELADO
p = float(input('Digite o valor do produto R$ '))
#avista = ( p / 100 ) * 85
avista = p - (p * 15 / 100) # quando for desconto coloca subtração
#prazo = (p / 100 ) * 122 # forma que eu coloquei diferente do professor
prazo = p + (p * 22 / 100) # quando for aumento de porcentagem coloca soma
print('O valor de pagamento á vista é de R${:.2f}'
      '\n seu valor a prazo é de R${:.2f}'.format(avista, prazo))



