'''
ESCREVA UM PROGRAMA QUE PERGUNTE O SÁLARIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO.
PARA SALÁRIOS SUPERIORES A R$1.250,00, CALCULE UM AUMENTO DE 10%.
PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%.
'''
sal = float(input('Digite o salario do funcionario em R$: '))
superior = sal + (sal / 100) * 10
inferior = sal + (sal / 100) * 15
if sal > 1250:
    print('O salario do funcionario é R${:.2f} e recebera um almento de 10% e ficara em R${:.2f}'.format(sal, superior))
else:
    print('O salario do funcionario é R${:.2f} e recebera um almento de 15% e ficara em R${:.2f}'.format(sal, inferior))