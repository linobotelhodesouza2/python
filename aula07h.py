#DESAFIOS
# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2METROS QUADRADOS.
l = float(input('Digite a Largura da parede: '))
a = float(input('Digite a Altura da parede: '))
ar = l * a
lt = ar / 2
print(' Sua parede tem a dimensão de {} x {} e sua área é de {:.2f}m²'
'\n Para pintar voçê vai precisar de {:.1f}l de tinta.'.format(l, a, ar, lt))



