'''
CRIE UM PROGRMA QUE LEIA UM NUMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU ÍMPAR.
'''

num = int(input('Digite um numero qualquer: '))
if (num % 2 == 1): # o numero de resto 2  for igual a 1 será impar caso o contrario sera par
    print('impar')
else:
    print('Par')
