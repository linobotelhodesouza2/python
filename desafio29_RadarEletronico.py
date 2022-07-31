'''
ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE.
'''
car = int(input('Digite a velocidade do veiculo em Km: '))
velMaior = (car - 80) * 7
if car > 80:
    print('Voçê atingiu a velocidade de {} Km, e será multado em R${:.2f} reais.'.format(car, velMaior))
else:
    print('Voçê esta na velocidade de {} Km e esta na velocidade permitida, siga assim.'.format(car, velMaior))
