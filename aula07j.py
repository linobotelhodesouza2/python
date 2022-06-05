#FAÇA UM ALGORITMO QUE LEIA O SALARIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO.
f = float(input('Insira o valor do seu sálario: '))
s = (f / 100) * 115
print('O seu salário é {:.2f} reais, seu novo salário com um aumento de 15% é {:.2f} reais.'.format(f, s))
