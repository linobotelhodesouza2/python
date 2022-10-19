'''
CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA COM UMA CONTAGEM POR EXTENSO, DE ZERO ATÉ
VINTE.
SEU PROGRAMA DEVERÁ LER UM NUMERO PELO TECLADO(ENTRE 0 E 20) E MOSTRÁ-LO POR EXTENSO.
'''
from time import sleep
numeros = (
'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
'catorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um Número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Voçê digitou o numero {numeros[num]}')
        usuario = str(input('Voçê deseja continuar? S/N ')).upper().strip()[0]
        if usuario == 'S':
            print('', end=' ')# se na digitar o numero dentro do while ele coloca o tente novamente sem pular linha com o end=''
        else:
            print('Finalizando o programa aguarde...')
            time = sleep(4)
            print('\nPrograma Finalizado!')
            break