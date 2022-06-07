#DESAFIO
#CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA.
#EX: DIGITE UM NUMERO: 6127
# O NUMERO 6127 TEM A PARTE INTEIRA 6.
import math #importando o modulo matematico
num = float(input('Digite um número qualquer: '))
inteira = math.floor(num) # colocando o modulo math e escolhendo somente o modulo de arredondamento para baixo
print('O número {} tem a parte inteira {}. '.format(num, inteira))

from math import floor # importando o modulo matematico mais somento o arredondamento para baixo com o floor
num = float(input('Digite um numero qualque: '))
inteira = floor(num) # inserindo somente o metodo floor na variavel num
print('O numero {} tem a parte inteira {}'.format(num, inteira))