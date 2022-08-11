'''
REFAÇA O DESAFIO 35 DOS TRIANGULOS ACRESCENTANDO O RECURSO DE MOSTRA QUE TIPO DE TRIANGULO SERÁ FORMADO:
-EQUILATERO: TODOS OS LADOS IGUAIS
-ISÓSCELES: DOIS LADOS IGUAIS
-ESCALENO:TODOS OS LADOS DIFERENTES
'''
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
if a < b + c and b < c + a and c < a + b:
    print('Os segmentos PODEM gerar um triângulo')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c:
        print('TRIANGULO ISOSCELES')
    elif a != b and b != c and c != a:
        print('TRIANGULO ESCALENO')
else:
    print('Os segmentos NÃO PODEM gerar um triângulo')

