'''
ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO CONSIDERANDO O SEU PRECO NORMAL E CONDIÇÃO
DE PAGAMENTO:
-A VISTA DINHEIRO / CHEQUE : 10% DE DESCONTO
-A VISTA NO CARTAO : 5% DE DESCONTO
- EM ATE 2X NO CARTAO : PRECO NORMAL
- 3X OU MAIS NO CARTAO : 20% DE JUROS
'''
print('{:=^40}'.format(' LOJA '))# colocando o nome no meio
prod = float(input('Digite o valor do Produto:R$'))
descD = prod - (prod / 100) * 10
descC = prod - (prod / 100) * 5
juros = prod + (prod / 100) * 20
print('''\nEscolha a forma de Pagamento:
[1] Dinheiro ou Cartão a Vista
[2] Cartão a Vista
[3] em até 2 vezes sem Juros no Cartão
[4] em mais de 3 vezes no Cartão com Juros
''')
escolha = int(input('Sua Escolha de Pagamento:'))
# A VISTA
if escolha == 1:
    print('O valor do Produto escolhido é R${:.2f} reais, e avista ficará R${:.2f} reais, tanto no Cheque ou Dinheiro,'
          'Obrigado.'.format(prod, descD))

# CARTAO A VISTA
elif escolha == 2:
    print('O valor do Produto escolhido é R${:.2f} reais, e avista no Cartão ficará R${:.2f} reais, '
          'Obrigado.'.format(prod, descC))

# EM 2x SEM JUROS
elif escolha == 3:
    print('Voçê pode parcelar em até 2 Vezes sem Juros no Cartão \nQuantas vezes voçê quer parcelar?')
    parcela = int(input('Sua Escolha: '))
    if parcela == 1:
        print('O valor do Produto escolhido é R${:.2f} reais, em 1 vez no Cartão será de R${:.2f} reais, '
              'Obrigado.'.format(prod, prod))
    elif parcela == 2:
        print('O valor do Produto escolhido é R${:.2f} reais, em 2 vezes de R${:.2f} reais no Cartão,'
              'Obrigado.'.format(prod, prod / 2))
    elif parcela > 2:
        print('Voçê digitou um valor de parcela que não exite, tente novamente,Obrigado.')

# EM MAIS DE 3x COM JUROS
elif escolha == 4:
    print('Voçê pode parcelar em até 10 vezes com juros no Cartão\nQuantas vezes voçê quer parcelar?')
    totalparc = int(input('Sua escolha em parcelas: '))
    if totalparc > 10:
        print('Voçê digitou um valor de parcela que não exite, tente novamente,Obrigado.')
    else:
        print('Sua compra será parcelada em {}x de R${:.2f} com JUROS'.format(totalparc, juros / totalparc))
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(prod, juros))
