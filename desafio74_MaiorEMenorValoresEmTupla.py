'''
CRIE UM PROGRAMA QUE VAI GERAR CINCO NUMEROS ALEATORIOS E COLOCAR EM UMA TUPLA.DEPOIS DISSO, MOSTRE A LISTAGEM
DE NUMEROS GERADOS E TAMBEM INDIQUE O MENOR E O MAIOR VALOR QUE ESTAO NA TUPLA..
'''
from random import randint #importando a biblioteca random e o metodo randint
n = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10)) #colocando a variavel de repetição dentro de uma tupla para que se tenha mais de uma repeticao nos valores aleatorios
print('Valores sorteados foram :', end='')
for numeros in n:
    print(f' {numeros}', end='') # criando um laço que poem os numeros dentro do range da tupla o end='' serve para deixar os valores afrente de cada um
print(f'\nO maior valor é {max(n)}')
print(f'O menor valor é {min(n)}')