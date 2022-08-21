'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
for p in range(1, 6):
    peso = float(input('Digite o {}° peso: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {} Kg '.format(maior))
print('O menor peso foi de {} Kg '.format(menor))
