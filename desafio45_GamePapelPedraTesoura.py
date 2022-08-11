'''
CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOÇÊ
'''
print('****'*10,'JOKENPÔ','****'*10)
print('''Faça a sua Escolha 
[1]PAPEL
[2]PEDRA
[3]TESOURA
''')
from random import randint
import time
escolha = int(input('Digite a sua escolha: '))
print('****'*10, 'JO', '****'*10)
t = 0.5
time.sleep(t)
print('****'*10, 'KEN', '****'*10)
t = 0.5
time.sleep(t)
print('****'*10, 'PÔ', '****'*10)
t = 0.5
time.sleep(t)

if escolha == 1:
    print('\no jogador escolheu PAPEL')
elif escolha == 2:
    print('\no jogador escolheu PEDRA')
elif escolha == 3:
    print('\no jogador escolheu TESOURA')

# COMP MAIS JOGADOR
num = randint(1, 3)
if num == 1:
    print('o computador escolheu PAPEL\n')
elif num == 2:
    print('o computador escolheu PEDRA\n')
elif num == 3:
    print('o computador escolheu TESOURA\n')

# QUEM GANHA E QUEM PERDE
print('****'*10)
# ESCOLHA UM
if escolha == 1 and num == 2:
    print('PAPEL GANHA DE PEDRA VOÇÊ GANHOU')
elif escolha == 1 and num == 3:
    print('PAPEL PERDE PARA TESOURA VOÇÊ PERDEU')
elif escolha == 1 and num == 1:
    print('OPS DEU EMPATE')
# ESCOLHA DOIS
if escolha == 2 and num == 1:
    print('PEDRA PERDE PARA PAPEL VOÇÊ PERDEU')
elif escolha == 2 and num == 3:
    print('PEDRA GANHA DA TESOURA VOÇÊ GANHOU')
elif escolha == 2 and num == 2:
    print('OPS DEU EMPATE')
# ESCOLHA TRES
if escolha == 3 and num == 1:
    print('TESOURA GANHA DO PAPEL VOÇÊ GANHOU')
elif escolha == 3 and num == 2:
    print('TESOURA PERDE PARA PEDRA VOÇÊ PERDEU')
elif escolha == 3 and num == 3:
    print('OPS DEU EMPATE')
'''
#RESOLUÇÂO DE OUTRA FORMA
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Qual a sua escolha?
[1]PAPEL
[2]PEDRA
[3]TESOURA
''')
jogador = int(input('Qual a sua jogada ?'))
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-='*12)
if computador == 0:# computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:    
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
if computador == 0:  # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
if computador == 0:  # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
'''