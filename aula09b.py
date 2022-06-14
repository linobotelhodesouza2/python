'''
DESAFIO
CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
- O NOME COM TODAS AS LETRAS MAISCULAS
- O NOME  COM TODAS MINUSCULAS
- QUANTAS LETRAS AOTODO SEM CONSIDERAR ESPACOS
- QUANTAS LETRAS TEM O PRIMEIRO NOME.
'''
n = str(input('Digite seu nome completo: ')).strip()# usando o '.strip' direto aqui para eliminar os espaços no campo de nome,strip remove os espaços excedentes
print('Analisando seu nome...')
print('Seu nome em maiscula é {}'.format(n.upper()))
print('Seu nome em minuscula é {}'.format(n.lower()))
print('Seu nome tem ao todo {} letras'.format(len(n) - n.count(' ')))# dessa forma o len conta quantas letras tem junto com o espaço porem eu uso o - n.count('  ') para retirar do contador o espaço atribuido ao nome
print('Seu primeiro nome tem {} letras'.format(n.find(' ')))
#outra forma de fazer
separa = n.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))







