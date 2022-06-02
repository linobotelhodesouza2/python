#Ordem de precedência
#1 ()
#2 **
#3 * / // %
#4 + -
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d), end= '')
print('A soma é {},\n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end= '')
# o \n pula uma linha ou seja nova linha , o {:.3f} é 3 casas decimais com ponto flutuante, o end='' é para nao quebrar uma linha se houver dois print´s vai ficar na mesma linha
print('Divisao inteira {} e potência {}'.format(di, e))
