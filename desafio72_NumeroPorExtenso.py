'''
CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA COM UMA CONTAGEM POR EXTENSO, DE ZERO ATÉ
VINTE.
SEU PROGRAMA DEVERÁ LER UM NUMERO PELO TECLADO(ENTRE 0 E 20) E MOSTRÁ-LO POR EXTENSO.
'''
numeros = (
'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
'catorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um Número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente', end= '')
print(f'Voçê digitou o numero {numeros[num]}')
