'''
FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E DIGA SE ELE É OU NAO UM NUMERO PRIMO
'''
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')# COR AZUL MOSTRANDO QUAL NUMERO É DIVISIVEL
        tot += 1
    else:
        print('\033[31m', end='')# COR VERMELHA MOSTRANDO QUAL NUMERO NAO É DIVISIVEL
    print('{} '.format(c), end='')
print('\n\033[m O número {} foi divisivel {} vezes'.format(num, tot))# CODIGO PARA ZERAR A COR E COLOCAR A BRANCA PADRÃO
if tot == 2:
    print('Número é PRIMO')
else:
    print('Número NÃO È PRIMO')