'''
CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOÇÊ
'''
print('****'*10,'JOKENPÔ','****'*10)
print('''Faça a sua Escolha: 
[1]PAPEL
[2]PEDRA
[3]TESOURA
''')
from random import randint
num = randint(1, 3)
print(num)
