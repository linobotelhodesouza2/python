# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2METROS QUADRADOS.
l = float(input('Digite a Largura da parede: '))
a = float(input('Digite a Altura da parede: '))
ar = l * a
lt = ar / 2
print('A área é de {:.2f} metros, e para pintar voçê vai precisar de {:.0f} litros de tinta.'.format(ar, lt))



