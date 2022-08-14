'''
FAÇA  UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE ARTIFICIO , INDO DE 10 ATÉ 0,
COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES.
'''
import time# importando a biblioteca time/////from time import sleep
t = 1
time.sleep(t)
for c in range(10, -1, -1):# sintaxe contador regressivo de 10 até 0  com um tempo de 1 seg entre eles
    t = 0.8
    time.sleep(t)
    print(c)
    if c == 0:
        print('\U0001F4A5 CHAZAAAANNN!!!!!')#codigo unicode explosão
