'''
DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM.
CALCULE O PREÇO DA PASSAGEM , COBRANDO R$0,50 POR KM PARA VIAGENS DE ATÉ 200KM E R$0,45 PARA VIAGENS MAIS LONGAS.
'''
v = float(input('Digite a distância em Km da sua viagem: '))
curta = v * 0.50
longa = v * 0.45
if v > 200:
    print('Sua viagem teve {}Km e sua passagem será de R${:.2f} reais.'.format(v, longa))
else:
    print('Sua viagem teve {}Km e sua passagem será de R${:.2f} reais.'.format(v, curta))