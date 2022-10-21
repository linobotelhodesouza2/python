'''
FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMERICOS E GUARDE-OS EM UMA LISTA.
NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR DIGITADO E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA.
'''
valores = []
maior = 0
menor = 0
for n in range(0, 5):
    valores.append(int(input(f'Digite um numero para a posição {n}: ')))
    if n == 0:
        maior = menor = valores[n]
    else:
        if valores[n] > maior:
            maior = valores[n]
        if valores[n] < menor:
            menor = valores[n]
print()
print(f'\nLista {valores}')
print()
print(f'O maior valor digitado foi {maior} na posiçao ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} na posiçao ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
