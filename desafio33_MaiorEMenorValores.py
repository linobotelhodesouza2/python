'''
FAÇA UM PROGRAMA QUE LEIA TRÊS NUMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR.
'''

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor foi {}'.format(menor))
print('O maior foi {}'.format(maior))
