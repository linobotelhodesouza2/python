'''
ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR 'PENSAR' EM UM NUMERO INTEIRO ENTRE 0 E 5 E PEÇA PARA O USUARIO DESCOBRIR QUAL FOI O NUMERO
ESCOLHIDO PELO COMPUTADOR.
O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUARIO VENCEU OU PERDEU.
'''
from random import randint
num = int(input('DIgite um numero de 1 a 5: '))
sorteio = randint(1, 5)
if num == sorteio:
    print('Voçê acertou, o numero digitado foi {} eu pensei no numero {}'.format(num, sorteio))
else:
    print('Voçê errou, voçê digitou {} e eu pensei no numero {}'.format(num, sorteio))
