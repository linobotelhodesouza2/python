'''
FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS VALORES 'M' OU 'F'.CASO ESTEJA ERRADO
,PEÇA A DIGITAÇÃO NOVAMENTE ATE TER UM VALOR CORRETO.
'''
sexo = str(input('Digite o seu sexo [M - F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
        sexo = str(input('Dados incorretos, digite o seu sexo [M - F]: ')).strip().upper()[0]
print('Sexo {}, registrado corretamente.'.format(sexo))
