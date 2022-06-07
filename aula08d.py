#DESAFIO
#FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE NA TELA O VALOR DE SENO,COSSENO E TANGENTES DESSE ANGULO.
#import math
#sen = float(input('Digite o valor de seno: '))
#cos = float(input('Digite o valor de cosseno: '))
#tg = math.atan2(sen, cos)
#print('O valor de seno foi {} e cosseno {}, sua tangente é {}.'.format(sen, cos, tg))

import math
tg = int(input('Digite um ângulo: '))
sen = math.sin(tg)
cos = math.cos(tg)
print('O valor do angulo de {} é seno {} e cosseno {}.'.format(tg, sen, cos))
