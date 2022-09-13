'''
CRIE UM PROGRAMA QUE LEIA NUMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR
 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL, MOSTRE QUANTOS NUMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELAS
 (DESCONSIDERANDO O FLAG).
'''
n = 0
cont = 0
soma = 0
while True:
    n = int(input('Digite um numero digite 999 para parar o comando: '))
    if n == 999:
        break
    else:
        cont += 1
        soma = soma + cont
print(f'Voce saiu e voçê tentou {cont} vezes e a soma dos numeros digitados é {soma} ')