'''
MELHOR O JOGO DO DESAFIO 28 ONDE O COMPUTADOR VAI 'PENSAR' EM UM NUMERO DE 0 A 10. SÓ QUE AGORA O JOGADOR
VAIR TENTAR ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL  QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENCER.
'''
from random import randint
from time import sleep
computador = randint(1, 10)
print('Olá eu sou seu computador ')
print('Pensei em um numero de 1 a 10, voçê consegue adivinhar? ')
jogador = int(input('Digite seu palpite: '))

print('Analizando a resposta...')
time = sleep(3)

print(computador)