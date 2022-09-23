'''
CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VARIOS PRODUTOS. O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO
VAI CONTINUAR OU NÃO . NO FINAL MOSTRE:
A- QUAL É O TOTAL GASTO NA COMPRA.
B- QUANTOS PRODUTOS CUSTAM MAIS DE 1000.
C- QUAL É O NOME DO PRODUTO MAIS BARATO.
'''
print('-' * 10, 'LEITOR DE PRODUTOS', '-' * 10)
cont = 0
total = 0
maior = 0
barato = 0
while True:
    nome = str(input('\nDigite o nome do produto: ')).upper()
    preco = float(input('Digite o valor do produto:R$ '))
    total += preco
    if preco > 1000:
        maior += 1
    if cont == 1:
        barato = preco
    else:
        if preco < barato:
            barato = preco
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
print(f'O seu gasto total foi de {total:.2f} Reais')
print(f'{maior} produto(s) custou mais de 1000 Reais.')
print(f'O {nome} foi o produto(s) mais barato e custou  {barato} Reais  .')
print('-' * 50)