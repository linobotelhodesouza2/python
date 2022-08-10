'''
ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO CONSIDERANDO O SEU PRECO NORMAL E CONDIÇÃO
DE PAGAMENTO:
-A VISTA DINHEIRO / CHEQUE : 10% DE DESCONTO
-A VISTA NO CARTAO : 5% DE DESCONTO
- EM ATE 2X NO CARTAO : PRECO NORMAL
- 3X OU MAIS NO CARTAO : 20% DE JUROS
'''
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

if escolha == 1:
    print('O valor do Produto escolhido é R${:.2f} reais, e avista ficará R${:.2f} reais, tanto no Cheque ou Dinheiro,'
          'Obrigado.'.format(prod, descD))
elif escolha == 2:
    print('O valor do Produto escolhido é R${:.2f} reais, e avista no Cartão ficará R${:.2f} reais, '
          'Obrigado.'.format(prod, descC))
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
elif escolha == 4:
    print('Voçê pode parcelar em até 10 vezes com juros no Cartão\nQuantas vezes voçê quer parcelar?')
    parcela = int(input('Sua escolha: '))
    if parcela == 1:
        print('O valor do Produto escolhido é R${:.2f} reais, em 1 vez no Cartão será de R${:.2f} reais, '
              'Obrigado.'.format(prod, juros))
    elif parcela == 2:
        print('O valor do Produto escolhido é R${:.2f} reais, em 2 vezes no Cartão será de R${:.2f} reais, '
              'Obrigado.'.format(prod, juros / 2))
    elif parcela == 3:
        print('O valor do Produto escolhido é R${:.2f} reais, em 3 vezes no Cartão será de R${:.2f} reais, '
              'Obrigado.'.format(prod, juros / 3))
    elif parcela == 4:
        print('O valor do Produto escolhido é R${:.2f} reais, em 4 vezes no Cartão será de R${:.2f} reais, '
              'Obrigado.'.format(prod, juros / 4))
    elif parcela == 5:
        print('O valor do Produto escolhido é R${:.2f} reais, em 5 vezes no Cartão será de R${:.2f} reais, '
              'Obrigado.'.format(prod, juros / 5 ))
    elif parcela == 6:
        print('O valor do Produto escolhido é R${:.2f} reais, em 6 vezes no Cartão será de R${:.2f} reais, '
              'Obrigado.'.format(prod, juros / 6))
    elif parcela == 7:
        print('O valor do Produto escolhido é R${:.2f} reais, em 7 vezes no Cartão será de R${:.2f} reais, '
              'Obrigado.'.format(prod, juros / 7))
    elif parcela == 8:
        print('O valor do Produto escolhido é R${:.2f} reais, em 8 vezes no Cartão será de R${:.2f} reais, '
              'Obrigado.'.format(prod, juros / 8))
    elif parcela == 9:
        print('O valor do Produto escolhido é R${:.2f} reais, em 9 vezes no Cartão será de R${:.2f} reais, '
              'Obrigado.'.format(prod, juros / 9))
    elif parcela == 10:
        print('O valor do Produto escolhido é R${:.2f} reais, em 10 vezes no Cartão será de R${:.2f} reais, '
              'Obrigado.'.format(prod, juros / 10))
    elif parcela > 10:
        print('Voçê digitou um valor de parcela que não exite, tente novamente,Obrigado.')
