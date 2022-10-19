'''
CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS (NÃO USAR ACENTOS).DEPOIS DISSO, VOÇÊ DEVE MOSTRAR,
PARA CADA PALAVRA, QUAIS SÃO AS SUAS VOGAIS.
'''
palavras = ('aprender', 'empreender', 'futuro', 'programar', 'python', 'windowns', 'computador', 'jovem',
            'surpreender', 'dev', 'dados', 'banco', 'javascript', 'vencer', 'dinheiro', 'passado')
for l in palavras:
    print(f'\nNa palavra {l.upper()} temos ', end='')
    for letra in l:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            