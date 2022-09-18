'''
FAÇA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O COMPUTADOR. O JOGO SÓ SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER,
MOSTRANDO O TOTAL DE VITÓRIAS CONSECULTIVAS QUE ELE CONQUISTOU NO FINAL DO JOGO.
'''
print('-' * 10, 'JOGO DO PAR OU IMPAR', '-' * 10)
from random import randint
v = 0
while True:
      jogador = int(input('Diga um valor: '))
      computador  = randint(0, 11)
      total = jogador + computador
      tipo =' '
      while tipo not in 'PI':
            tipo = str(input('Par ou Impar? [P/I]  ')).strip().upper()[0]
      print(f'Voçê jogou {jogador} e o computador jogou {computador}. Total de {total}')
      if tipo == 'P':
            if total % 2 == 0:
                  print('Voçê Venceu!')
                  v += 1
            else:
                  print('Voçê Perdeu!')
                  break
      elif tipo == 'I':
            if total % 2 == 1:
                  print('Voçê Venceu!')
                  v += 1
            else:
                  print('Voçê Perdeu!')
                  break
      print('Vamos jogar novamente...')
print(f'GAME OVER ! Voçê venceu {v} vezes.')