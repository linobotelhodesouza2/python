'''
CRIE UM PROGRAMA QUE TENHA UMA TUPLA UNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PREÇOS, NA SEQUÊNCIA.NO FINAL
,MOSTRE UMA LISTAGEM DE PREÇOS, ORGANIZANDO OS DADOS EM FORMA TABULAR.
'''
lista = ('Lapis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90,
         )
print('-'* 60)
print(f'{"LISTAGEM DE PREÇOS" : ^60}')
print('-'* 60)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<51}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-'* 60)
