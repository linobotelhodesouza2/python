'''
DESAFIO
CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
- O NOME COM TODAS AS LETRAS MAISCULAS
- O NOME  COM TODAS MINUSCULAS
- QUANTAS LETRAS AOTODO SEM CONSIDERAR ESPACOS
- QUANTAS LETRAS TEM O PRIMEIRO NOME.
'''
n = str(input('Digite seu nome: '))
print(n.upper())
print(n.lower())
print(len(n))
print(len(n.rstrip()))
print(n.split())
print(len(n.split()))









