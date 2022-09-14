'''
FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VARIOS NUMEROS ,UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUARIO.
O PROGRAMA SERÁ INTERROMPIDO QUANDO O NUMERO SOLICITADO FOR NEGATIVO.
'''
n = 0
resp = 'S'
while True:
    print('Calcule a Tabuada, se quiser sair é só colocar um numero negativo')
    n = int(input('Digite um numero: '))
    if n > 0:
        for tab in range(1, 11):
            s = n * tab
            print(f'{n} x {tab} = {s}')
    else:
        if n < 0:
            resp = str(input('Voçê quer continuar [S/N]? ')).upper()
            if resp == 'N':
                print('Até mais !')
                break


