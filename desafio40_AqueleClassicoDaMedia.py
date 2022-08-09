'''
CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MEDIA, MOSTRANDO UMA MENSAGEM NO FINAL
,DE ACORDO COM A MEDIA ATINGIDA:
-MEDIA ABAIXO DE 5.0 REPROVADO
-MEDIA ENTRE 5.0 E 6.9 RECUPERAÇAO
-MEDIA 7.0 OU SUPERIOR APROVADO
'''
aluno = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Aluno Reprovado')
elif media > 5 and media <= 6.9:
    print('Aluno em Recuperação')
elif media >= 7:
    print('Aluno Aprovado')
print('Ola {}, sua primeira nota foi {} e sua segunda foi {}, sua media foi {} '.format(aluno, n1, n2, media))

