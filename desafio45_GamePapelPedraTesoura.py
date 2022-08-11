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
print('****'*5,'JO','****'*5)
t = 1
time.sleep(t)
print('****'*5,'KEN','****'*5)
t = 1
time.sleep(t)
print('****'*5,'PÔ','****'*5)
t = 1
time.sleep(t)
if escolha == 1:
    print('\no jogador escolheu PAPEL')
elif escolha == 2:
    print('\no jogador escolheu PEDRA')
elif escolha == 3:
    print('\no jogador escolheu TESOURA')

# juntando o computador mais o jogador
num = randint(1, 3)
if num == 1:
    print('o computador escolheu PAPEL\n')
elif num == 2:
    print('o computador escolheu PEDRA\n')
elif num == 3:
    print('o computador escolheu TESOURA\n')

# logica de quem ganhou e quem perdeu
print('****'*10)
#ESCOLHA UM
if escolha == 1 and num == 2:
    print('PAPEL GANHA DE PEDRA VOÇÊ GANHOU')
elif escolha == 1 and num == 3:
    print('PAPEL PERDE PARA TESOURA VOÇÊ PERDEU')
elif escolha == 1 and num == 1:
    print('OPS DEU EMPATE')
#ESCOLHA DOIS
if escolha == 2 and num == 1:
    print('PEDRA PERDE PARA PAPEL VOÇÊ PERDEU')
elif escolha == 2 and num == 3:
    print('PEDRA GANHA DA TESOURA VOÇÊ GANHOU')
elif escolha == 2 and num == 2:
    print('OPS DEU EMPATE')
#ESCOLHA TRES
if escolha == 3 and num == 1:
    print('TESOURA GANHA DO PAPEL VOÇÊ GANHOU')
elif escolha == 3 and num == 2:
    print('TESOURA PERDE PARA PEDRA VOÇÊ PERDEU')
elif escolha == 3 and num == 3:
    print('OPS DEU EMPATE')