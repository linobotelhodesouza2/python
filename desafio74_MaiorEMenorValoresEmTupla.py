'''
CRIE UM PROGRAMA QUE VAI GERAR CINCO NUMEROS ALEATORIOS E COLOCAR EM UMA TUPLA.DEPOIS DISSO, MOSTRE A LISTAGEM
DE NUMEROS GERADOS E TAMBEM INDIQUE O MENOR E O MAIOR VALOR QUE ESTAO NA TUPLA..
'''
from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Valores sorteados foram :', end='')
for numeros in n:
    print(f' {numeros}', end='')
print(f'\nO maior valor é {max(n)}')
print(f'O menor valor é {min(n)}')