#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 17:48:47 2022

@author: lino
"""
'''
REFAÇA O DESAFIO 51, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA, MOSTRANDO
OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE.
'''
#Primeiro Modelo
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao
#for c in range(0, 11, 1):
for c in range(primeiro, decimo + razao, razao):
     print('{}'.format(c), end=' \U0000279C ')
print('Fim')

#Segundo Modelo
print('Gerador de PA')
print('***' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')

