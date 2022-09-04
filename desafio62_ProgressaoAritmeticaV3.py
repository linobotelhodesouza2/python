#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 17:48:47 2022

@author: lino
"""
'''
MELHORE O DESAFIO 61 PERGUNTANDO PARA O USUARIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS.
O PROGRAMA ENCERRARÁ QUANDO ELE DISSER QUE QUER MOSTRAR 0 TERMOS.
'''
print('Gerador de PA')
print('***' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressao finalizada com {} termos mostrados.'.format(total))

