'''
CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VARIOS PRODUTOS. O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO
VAI CONTINUAR OU NÃO . NO FINAL MOSTRE:
A- QUAL É O TOTAL GASTO NA COMPRA.
B- QUANTOS PRODUTOS CUSTAM MAIS DE 1000.
C- QUAL É O NOME DO PRODUTO MAIS BARATO.
'''
print('-' * 10, 'LEITOR DE PRODUTOS', '-' * 10)
cont = 0
while True:
    nome = str(input('Digite o nome do produto: ')).upper()
    preco = int(input('Digite o valor do produto:R$ '))

    resp = ' '
    while resp not in 'SN':
        print('-' * 50)
        resp = str(input('Deseja continuar cadastrando [S/N]: ')).strip().upper()[0]
        if resp == 'S':
            cont += 1

    if resp == 'N':
        print('Obrigado.')
        cont += 1
        break


print('-' * 50)
print(f'\nVoçê cadastrou {cont} produto(s).')
print('-' * 50)
print(f'Produto: ........................{nome}')
print(f'Preço: ..........................R${preco}')
print('-' * 50)