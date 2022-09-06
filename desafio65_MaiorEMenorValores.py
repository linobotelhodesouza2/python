'''
CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS NO TECLADO. NO FINAL DA EXECUÇÃO, MOSTRE A MEDIA ENTRE TODOS
OS VALORES E QUAL FOI O MAIOR E O MENOR VALORES LIDOS. O PROGRAMA DEVE PERGUNTAR AO USUARIO SE ELE QUER OU NAO
CONTINUAR A DIGITAR VALORES.
'''
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} numeros e a media foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))