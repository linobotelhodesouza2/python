'''
FAÇA UM PROGRAMA QUE LEIA UM NUMERO QUALQUER E MOSTRE O SEU FATORIAL
'''
#primeira forma de fazer utilizando a biblioteca matematica

from math import factorial
n = int(input('Digite um numero para calcular o seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))

#segunda forma de fazer sem utilizar a biblioteca e mostrando os valores passo a passo

n = int(input('Digite um numero para calcular o seu fatorial: '))
c = n 
f = 1

print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
