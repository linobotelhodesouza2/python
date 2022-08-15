'''
CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS.NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO
ATINGIRAM A MAIORIDADE E QUANTOS JÁ SÃO MAIORES.
'''
from datetime import date
atual = date.today().year
totalMaior = 0
totalMenor = 0
for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc
    #print('Essa pessoa tem {} anos'.format(idade))
    if idade >= 21:
        totalMaior += 1
        #print('Essa pessoa é maior de idade')
    else:
        totalMenor += 1
        #print('Essa pessoa não é maior de idade')
print('Ao todo tivemos {} pessoa maior de idade'.format(totalMaior))
print('Ao todo tivemos {} pessoa maior de idade'.format(totalMenor))
