'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo
qual é o nome do homem mais velho e
quantas mulheres têm menos de 20 anos.
'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for c in range(1, 5):
    #print('-----'{}' PESSOA ------'.format(c))
    print('---' * 10)
    nome = str(input('Digite o nome da {}° pessoa: '.format(c))).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M - F]: ')).strip()
    #lendo a soma das idades
    somaidade += idade #somaidade = somaidade + idade ou simplificado com somaidade += idade
    # lendo o nome e a idade do homem mais velho
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    #lendo o total de mulheres com idade ate 20 anos
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos .'.format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos.'.format(nomevelho, maioridadehomem))
print('Ao todo é {} mulher(s) com menos de 20 anos.'.format(totmulher20))