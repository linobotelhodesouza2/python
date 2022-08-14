'''
ESTRUTURA DE REPETIÇÃO FOR, ITERAÇÃO
for c in range(6, -1, -1):
    print(c)
contagem regressiva de 6 ate 0

for c in range(1, 7, 1):
    print(c)
contagem de 0 ate 6

n = int(input('Digite um numero: '))
for c in range(n, 10):
    print(c)
mostra um numero de n ate 10

n = int(input('Digite um numero: '))
for c in range(0, n):
    print(c)
mostra de 0 ate 'n' o numero digitado

inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
for c in range(inicio, fim+1, passo):
    print(c)
mostra o valor inicial e final pulando de 'passo' um numero determinado para pular ate chegar ao final

for c in range(0, 5):
    n = int(input('Digite um valor: '))
colocando um input dentro do for

s = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    s += n
print('O somatorio dos valores foi {}.'.format(s))
colocando um valor inicial de zero e somando aos valores digitados e finalizando com o valor.
'''
s = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    s += n
print('O somatorio dos valores foi {}.'.format(s))
