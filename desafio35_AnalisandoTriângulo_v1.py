'''
DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUÁRIO SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO.
triangulo e formado quando a soma dos dois lados for menor que a de um dos lados 
'''
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
if a < b + c and b < c + a and c < a + b:
    print('Os segmentos PODEM gerar um triângulo')
else:
    print('Os segmentos NÃO PODEM gerar um triângulo')
