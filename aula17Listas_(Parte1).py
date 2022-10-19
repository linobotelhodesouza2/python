'''
VARIAVEIS COMPOSTAS LISTAS PARTE 1
TUPLAS () SÃO IMUTÁVEIS
LISTAS [] NÃO SÃO MUTÁVEIS

APPEND() ADICIONA UM ELEMENTO A LISTA
INSERT() ADICIONA NA POSIÇÃO QUE SE QUER

DEL[] APAGAR UM ELEMENTO
POP() APAGAR UM ULTIMO OU O INDICE QUE SE QUER APAGAR
REMOVE() REMOVE UM ELEMENTO PELO CONTEUDO

SORT() ORDENA OS VALORES
SORT(REVERSE=TRUE) ORDENA NA ORDEM REVERSA
LEN() MOSTRA QUANTOS ELEMENTOS EXISTE
'''
num = [1, 5, 3, 2, 8, 9] # criando uma lista
print(num)
num[2] = 7 # trocando o elementro 2 por 7
print(num)
num.append(12)# acrenscentando mais um numero ao final da lista
print(num)
num.sort()# deixando os valores em ordem crescente
print(num)
num.insert(2, 14) # inserindo um elemento na posição de indice 2 que acrescenta o 14
print(num)
num.pop() # retira o ultimo elemento da lista se não for passado nenhum paramêtro de eliminação
print(num)
num.pop(4) # eliminou o elemento na posição de indice 4 ou seja o numero 7
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.insert(5, 5)
print(num)
num.remove(5) # elementos iguais o remove pega a primeira ocorrência e retira o valor que estava primeiro.
print(num)
if 12 in num:
    num.remove(12)
else:
    print('Numero não esta na lista\n')

# criando uma lista vazia
#valores = list()
valores = [] # criando uma lista
valores.append(5) # acrescentando valores a minha lista com o metodo append
valores.append(8)
valores.append(3)

for v in valores: # pegue os valores em v no intervalo de valores e printe o v
    print(f'{v}...', end='')
print('\n')
for c, v in enumerate(valores): # os valores da chave e valor eu coloco um enumerate dos meus valores listados e coloco de forma de listagem chave e valor
    print(f'Na posição {c} encontrei o valor {v}!')
print('\nCheguei ao final da lista !!!')

print('\n')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores): # os valores da chave e valor eu coloco um enumerate dos meus valores listados e coloco de forma de listagem chave e valor
    print(f'Na posição {c} encontrei o valor {v}!')
print('\nCheguei ao final da lista !!!')

print('\n')

a = [2, 3, 4, 7]
b = a # desse modo a uma ligação entre as duas lista quando modificado o valor de B se modificara tambem o valor de A
b[2] = 8
print(f'Lista A {a}')
print(f'Lista B {b}')

print('\n')

a = [2, 3, 4, 7]
b = a[:] # desse modo é feito uma copia da lista A e os valores de B podem mudar sem alteração na lista A
b[2] = 8
print(f'Lista A {a}')
print(f'Lista B {b}')





