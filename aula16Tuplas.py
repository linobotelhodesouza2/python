# lanche = ()tupla []lista {}dicionario
#tupla são imutaveis
lanche = ('haburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])
#######################################
print('---'* 30)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
#######################################
print('---'* 30)

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
#######################################
print('---'* 30)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')
#######################################
print('---'* 30)

lanche = ('haburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Fritas')

print(sorted(lanche))
print(lanche)


#######################################
print('---'* 30)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5))
print(c.count(4))
print(c.count(9))
print(c)
print(c.index(8))
print(c)
print(c.index(4))
print(c)
print(c.index(2))
print(c)
print(c.index(5))
print(c)
print(c.index(5, 1))

pessoa = ('Lino', 39, 'M', 99.88)
print(pessoa)

pessoa = ('Lino', 39, 'M', 99.88)
del(pessoa)# apagando a tupla inteira
print(pessoa)
