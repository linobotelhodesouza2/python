#MANIPULANDO TEXTOS
#FATIAMENTO
s = 'Curso em Video Python'
print(s[9::3]) #pula de tres em tres e a primeira posicao é em V
#ANALISE
print(len(s)) mostra a quantidade de todos os caracteres existentes
print(s.count('o', 0, 13)) #mostra o valor 1 pois procura a letra 'o' e so tem uma em posicao 4 e a posicao 13 nao vale pois antecipa uma ficando na posicao 12
print(s.find('deo')) #mostra na tela aonde comeca a palavra procurada no caso posicao 11
print(s.find('Android')) #mostra um valor negativo, pois nao tem a palavra procurada
print('Curso'in(s)) #mostra se a condição é verdadeira
#TRANSFORMAÇÂO
print(s.replace('Python', 'Android')) # muda o nome python por android
print(s.upper()) # deixa as letras em caixa alta maiscula
print(s.lower()) # deixa tudo em minuscula
print(s.capitalize()) # deixa somente o primeiro caractere maiscula
print(s.title()) # Deixe os primeiros caracteres de cada palavra em maiscula
s = '   Aprenda Python    '
print(s.strip()) # Remove os espaços excedentes
print(s.rstrip()) # remove somente os ultimos espaços e nao do começo
print(s.lstrip()) # remove somente os primeiros espaços
#DIVISAO
s = 'Curso em Video Python'
print(s.split()) # divide a string entre os espaços e forma uma especie de lista
print('-'.join(s)) # junta todos os elementos de frase separados pelo split porem deixa cada letra com um caractere'-' como separador


