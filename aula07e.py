#ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS
m = int(input('Digite  valor em metros: '))
cent = m * 100
mil = m * 1000
print('O valor digitado em metros foi {}m, seu valor em centimetros é {}cm, e o valor em milimetros é {}mm'.format(m, cent, mil))

