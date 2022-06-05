#DESAFIOS
#DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE A SUA MÉDIA
aluno = input('Digite o nome do Aluno:  ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('O aluno {} teve a média {:.1f}'.format(aluno, ((n1+n2)/2)))


