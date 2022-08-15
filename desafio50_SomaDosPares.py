'''
DESENVOLVA UM PROGRAMA QUE LEIA SEIS NUMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES.
SE O VALOR DIGITADO FOR IMPAR DESCONSIDERE-O.

for c in range(1, 7):
    n = int(input('Digite um numero: '))
    m = int(input('Multiplicar por: '))
    s = n * m
    if n * m % 2 == 0:
        print('Par')

    print('A soma de {} x {} é {}'.format(n, m, s))
'''
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o valor {}: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Voçê informou {} numeros PARES e a soma foi {}'.format(cont, soma))
