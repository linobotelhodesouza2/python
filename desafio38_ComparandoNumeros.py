'''
ESCREVA UM PROGRAMA QUE LEIA DOIS NUMEROS INTEIROS E COMPARE-OS MOSTRANDO NA TELA UMA MENSAGEM :
- O PRIMEIRO VALOR É MAIOR
- O SEGUNDO VALOR É MAIOR
- NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS
'''
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('O primeiro numero {} é MAIOR'.format(n1))
elif n1 < n2:
    print('O segundo numero {} é MAIOR'.format(n2))
elif n1 == n2:
    print('Os dois numeros são iguais {} e {}.'.format(n1, n2))
