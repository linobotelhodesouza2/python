'''
FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NUMEROS IMPARES QUE SÃO MULTIPLOS DE TRES E QUE SE ENCONTRAM
NO INTERVALO DE 1 A 500
# acumulador s começa em 0 e quando o contador chegar no numero que se quer ele pega o numero inicial
#s = s + o contador c
'''
soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        '''print(c, end=' ')'''
        soma = soma + c
        cont =  cont + 1
print('\nA soma de todos os {} numeros é {}'.format(cont, soma))