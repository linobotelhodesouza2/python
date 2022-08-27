'''
CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU COMO AO LADO NA TELA:
SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇ~~AO SOLICITADA EM CADA CASO.
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
'''
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
print('==='* 10)
print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
''')

sair = False
while not sair:
    opcao = int(input('Digite a sua opção: '))
    if opcao == 1:
        print('Opção escolhida foi Somar os valores\nA soma fica {} + {} = {}'.format(n1, n2, n1 + n2))
        print('==='* 10)
        print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
''')

    if opcao == 2:
        print('Opção escolhida foi Multiplicar os valores\nA multiplicação fica {} x {} = {}'.format(n1, n2, n1 * n2))
        print('===' * 10)
        print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
''')

    if opcao == 3:
        if n1 > n2:
            print('Opção escolhida foi Maior dos valores\nO maior valor é {} '.format(n1))
            print('===' * 10)
            print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
''')
        else:
            print('Opção escolhida foi Maior dos valores\nO maior valor é {} '.format(n2))
            print('===' * 10)
            print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
''')

    if opcao == 4:
        print('==='* 10)
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
        print('Opção escolhida foi novos numeros')
        print('==='* 10)
        print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
''')
    elif opcao == 5:
        sair = True
print('Sua opção foi sair')
print('Foi bom ter voçê aqui , até mais.')
