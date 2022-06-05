#DESAFIOS
#FAÇA UM ALGORITMO QUE LEIA O SALARIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO.
f = float(input('Insira o valor do seu sálario R$ '))
s = (f / 100) * 115 # forma que eu pensei diferente mais que tambem funcionou
#s = s + (s * 15 / 100) forma que eu nao tinha pensado
print('O seu salário é R${:.2f}, seu novo salário com um aumento de 15% é R${:.2f} reais.'.format(f, s))
