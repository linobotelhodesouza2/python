#DESAFIO
#UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO.FAÇA UM PROGRAMA QUE AJUDE ELE,
#LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO.
import random
al1 = str(input('digite o nome do primeiro aluno: '))
al2 = str(input('digite o nome do segundo aluno: '))
al3 = str(input('digite o nome do terceiro aluno: '))
al4 = str(input('digite o nome do quarto aluno: '))
num = random.choice([al1, al2, al3, al4]) #metodo choice e matriz para puxar os valores correspondente das strings
print('O aluno escolhido foi o {}.'.format(num))

