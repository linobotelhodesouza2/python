'''
DESAFIO
FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ULTIMO NOME
SEPARADAMENTE.
EX: ANA MARIA DE SOUZA
PRIMEIRO:ANA
ULTIMO:SOUZA
'''
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()# split fatia a str em forma de lista
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu ultimo nome é {}.'.format(nome[len(nome)-1]))# -1 é sempre o ultimo nome
#Outra forma de se fazer sem o len
print('Seu ultimo nome é {}.'.format(nome[-1]))
