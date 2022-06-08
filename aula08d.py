'''DESAFIO
FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE NA TELA O VALOR DE SENO,COSSENO E TANGENTES DESSE ANGULO.
import math
sen = float(input('Digite o valor de seno: '))
cos = float(input('Digite o valor de cosseno: '))
tg = math.atan2(sen, cos)
print('O valor de seno foi {} e cosseno {}, sua tangente é {}.'.format(sen, cos, tg))
'''
#FORMA CORRETA
import math
ang = float(input('Digite um angulo: '))
sen = math.sin(math.radians(ang)) # TEM QUE CONVERTER O SENO EM RADIANOS UTILIZANDO O .MATH.RADIANS
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O valor do angulo de {} é: \n seno {:.2f} \n cosseno {:.2f} \n tangente {:.2f}.'.format(ang, sen, cos, tg ))

