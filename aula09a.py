'''
manipulando textos
'''

s = 'Curso em Video Python'
print(s[9::3]) #pula de tres em tres e a primeira posicao é em V
print(s.count('o', 0, 13)) #mostra o valor 1 pois procura a letra 'o' e so tem uma em posicao 4 e a posicao 13 nao vale pois antecipa uma ficando na posicao 12
print(s.find('deo')) #mostra na tela aonde comeca a palavra procurada no caso posicao 11
print(s.find('Android')) #mostra um valor negativo, pois nao tem a palavra procurada
print('Curso'in(s)) #mostra se a condição é verdadeira
