'''
DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO E GUARDE-OS EM UMA TUPLA.NO FINAL,MOSTRE:
A- QUANTAS VEZES APARECEU O VALOR 9
B- EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3
C- QUAIS FORAM OS NUMEROS PARES

'''

num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')))
print('Voçê digitou os valores:', end='')
for numeros in num:
    print(f' {numeros}', end='')
print(f'\nO valor 9 apareceu {num.count(9)} vez (s)')# mostra a contagem de quantas vezes o numero 9 apareceu
if 3 in num:
    print(f'A posição do primeiro valor 3 foi {num.index(3)+ 1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram os numero(s): ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
    