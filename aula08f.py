#DESAFIO
#O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS.
#FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA.
import random
al1 = str(input('Digite o nome do primeiro aluno: '))
al2 = str(input('Digite o nome do segundo aluno: '))
al3 = str(input('Digite o nome do terceiro aluno: '))
al4 = str(input('Digite o nome do quarto aluno: '))
s = random.shuffle(random[al1, al2, al3, al4])
print('A ordem sorteada dos alunos é {},{},{},{}.'.format(al1, al2, al3, al4))
