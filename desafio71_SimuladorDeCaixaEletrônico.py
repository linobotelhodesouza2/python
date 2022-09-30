'''
CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO.NO INICIO, PERGUNTE AO USUÁRIO QUAL SERÁ O
VALOR A SER SACADO ( NUMERO INTEIRO) E O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES.
OBS:.CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE $50,$20,$10,$1.
'''
print('-' * 50)
print('{:^50}'.format('CAIXA ELETRÔNICO'))
print('-' * 50)
valor = int(input('\nVALOR A SER SACADO: '))
total = valor   #variavel criada para receber o valor total do caixa
cedula = 50 # variavel cedula que vai receber o valor maximo possivel de saque do caixa
totalcedula = 0 # variavel que recebe o total de cedulas possiveis que começa em zero
while True: # enquanto verdadeiro faça
    if total >= cedula: # se o total de cedulas que eu quero sacar for maior ou igual a cedula possivel que e 50
        total -= cedula # eu vou ter o total que vai ser o valor total que eu quero sacar menos a cedula maior possivel que e 50
        totalcedula += 1 # o totalcedula vai receber entao como um contador e vai falar que o totalcedula recebeu mais uma cedula possivel de 50
    else: # se nao
        if totalcedula > 0: # se o total de cedula for maior que zero
            print(f'O total de {totalcedula} cedulas  de R${cedula} Reais') # printe na tela o valor de total de cedulas possiveis de tal cedula
        if cedula == 50: # se a cedula possivel for 50 me diga quantas se o maximo for atingido passe para a de 20
            cedula = 20
        elif cedula == 20:  # se a cedula possivel for a de 20 maximo passe para a de 10
            cedula = 10
        elif cedula == 10:  # se a cedula possivel for a de 10 maximo passe para a de 1
            cedula = 1
        totalcedula = 0 # se o total de cedulas possiveis for atingida com a de 1 e zerar e o total for igual a zero pare o programa com o break
        if total == 0:
            break
print('Volte sempre.')
