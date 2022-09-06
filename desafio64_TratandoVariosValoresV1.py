'''
CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO.O PROGRAMA SÓ VAI PARAR QUANDO O USUARIO DIGITAR
O VALOR 999, QUE É A CONDIÇÃO DE PARADA.NO FINAL,MOSTRE QUANTOS NUMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE
ELES (DESCONSIDERANDO O FLAG)
'''
num = cont = soma = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para parar]: '))
print('Voçe digitou {} numeros e a soma entre eles é {}.'.format(cont, soma))