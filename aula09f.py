'''
DESAFIO
FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
-QUANTAS VEZES APARECE A LETRA A
-EM QUE POSICAO ELA APARECE A PRIMEIRA VEZ
-EM QUE POSICAO ELA APARECE A ULTIMA VEZ
'''
f = str(input('Digite sua frase: ')).upper().strip()
print('A letra A apareceu {} vezes.'.format(f.count('A')))
print('A letra A apareceu  na posição {}'.format(f.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(f.rfind('A')+1))# procura do lado right e mostra a ultima letraa