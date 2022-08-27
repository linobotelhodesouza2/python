'''
CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU COMO AO LADO NA TELA:
SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇ~~AO SOLICITADA EM CADA CASO.
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
'''

from time import sleep
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
print('===' * 10)
opcao = 0
while opcao != 5:
        print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
''')
        opcao = int(input('Digite a sua opção: '))
        if opcao == 1:
                soma = n1 + n2
                print('Opção escolhida foi Somar os valores\nA soma fica {} + {} = {}'.format(n1, n2, soma))
                print('===' * 10)
        elif opcao == 2:
                mult = n1 * n2
                print('Opção escolhida foi Multiplicar os valores\nA multiplicação fica {} x {} = {}'.format(n1,
                                                                                                             n2,
                                                                                                             mult))
                print('===' * 10)
        elif opcao == 3:
                if n1 > n2:
                        maior = n1
                        print('Opção escolhida entre os valores\nO maior valor é {} '.format(n1))
                else:
                        maior = n2
                        print('Opção escolhida entre os valores\nO maior valor é {} '.format(n2))
                        print('===' * 10)
        elif opcao == 4:
                print('Digite os numeros novamente')
                print('===' * 10)
                n1 = int(input('Digite o primeiro numero: '))
                n2 = int(input('Digite o segundo numero: '))
                print('Opção escolhida foi novos numeros')
                print('===' * 10)
        elif opcao == 5:
                print('Estamos finalizando o programa...')
                sleep(5)
        else:
                print('Opção inválida, tente novamente!')
print('Foi bom ter voçê aqui , até mais.')