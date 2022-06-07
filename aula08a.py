#math modulo matematico
#ceil arredondamento para cima
#floor arredondamento para baixo
#trunc
#pow
#sqrt
#factorial
#import math importa o modulo completo
#from math import sqrt só usa a funcionalidade sqrt do modulo math

import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, math.floor(raiz)))

from math import sqrt
num = int(input('Digite um numero: '))
raiz =sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

import random
num = random.randint(1, 10)
print(num)

import emoji
print(emoji.emojize('Ola mundo :sunglasses:', use_aliases=True))

import emoji
print(emoji.emojize('Ola mundo :earth_americas:', use_aliases=True))


