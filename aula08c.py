#DESAFIO
#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM  TRIANGULO RETANGULO
#, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.
import math
c_op = float(input('Digite o valor do  cateto oposto: '))
c_adj = float(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(c_op, c_adj) # hipotenusa vai ser calculada pelo metodo de hipy que existe no modulo math
print('O valor da hipotenusa é {}.'.format(hip))
