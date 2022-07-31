'''
FAÇA UM PROGRAMA UE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO.

Primeira situação: Se o ano de 2015 ou 2016 for uma divisão exata em relação a 4, deveremos verificar, em seguida, se não é divisível por 100. Se não for, o ano será bissexto;
Segunda situação: Se o ano de 2015 ou 2016 não for divisível por 4, então deveremos verificar se ele é divisível por 400. Se também não for divisível, o ano de 2015 não será bissexto;
Terceira situação: Se o ano de 2015 ou 2016 não for divisível por 4, então devemos verificar se ele é divisível por 400. Caso seja, o ano de 2015 é bissexto.
'''

ano = int(input('Digite o ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('Ano bissexto.')
else:
    print('Não é um ano bissexto.')