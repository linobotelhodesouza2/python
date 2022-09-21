'''
CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VARIAS PESSOAS. A CADA PESSOA CADASTRADA , O PROGRAMA DEVERÁ
PERGUNTAR SE O USUÁRIO QUER OU NÃO CONTINUAR.NO FINAL,MOSTRE:
A- QUANTAS PESSOAS TEM MAIS DE 18 ANOS.
B- QUANTOS HOMENS FORAM CADASTRADOS.
C- QUANTAS MULHERES TEM MENOS DE 20 ANOS.
'''
print('-' * 10, 'CADASTRO DE PESSOAS', '-' * 10)
total = 0
totH = 0
totM20 = 0
cont = 1
while True:
        idade = int(input('Digite sua idade: '))
        sexo = ' '
        while sexo not in 'FM':
                sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
        if idade >= 18:
                total += 1
        if sexo == 'M':
                totH += 1
        if sexo == 'F' and idade < 20:
                totM20 += 1

        resp = ' '
        while resp not in 'SN':
                resp = str(input('Deseja continuar cadastrando [S/N]? ')).strip().upper()[0]
                if resp == 'S':
                        cont += 1
        print('-' * 41)
        if resp == 'N':
                print('Obrigado por cadastrar.')
                print('-' * 41)
                break
print(f'Voçê já cadastrou {cont} pessoas.')
print(f'Pessoas com mais de 18 anos:{total}.')
print(f'Voçê cadastrou {totH} homens.')
print(f'Voçê cadastrou {totM20} mulheres com menos de 20 anos.')