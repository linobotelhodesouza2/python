'''
ESCREVA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E PEÇA PARA O USUARIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO:
-1 PARA BINARIO
-2 PARA OCTAL
-3 PARA HEXADECIMAL
'''
num = int(input('Digite um numero: '))
print('''Digite uma opção para a conversão abaixo:
[1] Binario
[2] Octal
[3] Hexadecimal''')
conv = int(input('Sua Escolha: '))
if conv == 1:
    print('O numero {}, fica {} em Binário.'.format(num, bin(num)[2:]))
elif conv == 2:
    print('O numero {}, fica {} em Octal.'.format(num, oct(num)[2:]))
elif conv == 3:
    print('O numero {}, fica {} em Hexadecimal.'.format(num, hex(num)[2:]))
