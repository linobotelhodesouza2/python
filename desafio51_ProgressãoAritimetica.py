'''
DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA.NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS
DESSA PROGRESSÃO.
an = a1 + (n - 1) * r
soma da pa
sn = (a1 + an) * n / 2
'''
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao
#for c in range(0, 11, 1):
for c in range(primeiro, decimo + razao, razao):
     print('{}'.format(c), end=' \U0000279C ')
print('Fim')


