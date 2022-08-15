'''
CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALINDROMO, DESCONSIDERANDO OS ESPAÇOS
'''
frase = str(input('Digite a frase: ')).strip().upper()# strip Remove os espaços excedentes remove os espaços inuteis primeiros e ultimos, upper deixa a frase em letra maiscula
palavras = frase.split()# divide a string entre os espaços e forma uma especie de lista
junto = ''.join(palavras)# junto a frase digitada
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('A frase é um Palíndromo')
else:
    print('A frase não é um Palindromo')