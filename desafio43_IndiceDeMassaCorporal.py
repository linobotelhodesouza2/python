'''
DESENVOLVA UMA LOGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULE SEU IMC E MOSTRE SEU STATUS , DE ACORDO
COM A TEBELA ABAIXO:
-ABAIXO DE 18.5 : ABAIXO DO PESO
-ENTRE 18.5 E 25 : PESO IDEAL
-25 ATE 30 : SOBREPESO
-30 ATE 40 : OBESIDADE
-ACIMA DE 40 : OBESIDADE MÓRBIDA
IMC = PESO / (ALTURA * ALTURA)
'''
p = float(input('Digite o seu peso: '))
alt = float(input('Digite a sua altura: '))
imc = p / (alt * alt)
if imc < 18.5:
    print('Voçê tem {:.2f} de IMC e está ABAIXO DO PESO'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Voçê tem {:.2f} de IMC e está PESO IDEAL'.format(imc))
elif imc >= 25 and imc <= 30:
    print('Voçê tem {:.2f} de IMC e está com SOBREPESO'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Voçê tem {:.2f} de IMC e está com OBESIDADE'.format(imc))
elif imc > 40:
    print('Voçê tem {:.2f} de IMC e está com OBESIDADE MÓRBIDA'.format(imc))