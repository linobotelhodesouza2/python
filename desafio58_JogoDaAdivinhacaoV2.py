'''
MELHOR O JOGO DO DESAFIO 28 ONDE O COMPUTADOR VAI 'PENSAR' EM UM NUMERO DE 0 A 10. SÓ QUE AGORA O JOGADOR
VAIR TENTAR ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL  QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENCER.
'''
from random import randint
from time import sleep
computador = randint(1, 10)
print('Olá eu sou seu computador ')
print('Pensei em um numero de 1 a 10, voçê consegue adivinhar? ')

acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Digite seu palpite: '))
    palpite += 1
    print('Analizando sua resposta ......')
    time = sleep(3)
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Maior...')
        elif jogador > computador:
            print('Menor...')

   # print('O computador pensou em {} e voçê pensou {}'.format(computador, jogador))
print('Voçê acertou em {} tentativas.'.format(palpite))
