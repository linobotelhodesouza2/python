'''
A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE
SUA CATEGORIA, DE ACORDO COM A IDADE:
-ATE 9 ANOS : MIRIM
-ATE 14 ANOS : INFANTIL
-ATE 19 ANOS :JUNIOR
-ATE 20 ANOS : SENIOR
-ACIMA : MASTER
'''
from datetime import date
today = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = today - nasc
if idade <= 9:
    print('Sua idade é {} anos e sua Categoria é MIRIM.'.format(idade))
elif idade <= 14:
    print('Sua idade é {} anos e sua Categoria é INFANTIL.'.format(idade))
elif idade <= 19:
    print('Sua idade é {} anos e sua Categoria é JÚNIOR'.format(idade))
elif idade == 20:
    print('Sua idade é {} anos e sua Categoria é SENIOR'.format(idade))
elif idade > 20:
    print('Sua idade é {} anos e sua Categoria é MASTER'.format(idade))