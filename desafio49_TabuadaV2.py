'''
REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NUMERO QUE O USUARIO ESCOLHER, SÓ QUE AGORA
UTILIZANDO O LAÇO FOR
'''
n = int(input('Digite um numero: '))
for c in range(n * 0, 11, 1):
    print('{} x {:2} = {}'.format(n, c, n * c))
