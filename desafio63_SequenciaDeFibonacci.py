#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 17:48:47 2022

@author: lino
"""
''' 
 ESCREVA UM PROGRAMA QUE LEIA UM NUMERO N INTEIRO QUALQUER E MOSTRE NA 
 TELA OS N PRIMEIROS ELEMENTOS DE UMA SEQUENCIA DE FIBONACCI.
 F n = F n - 1 + F n - 2 
'''

print('Gerador de Fibonacci')
print('***' * 10)
n = int(input('Quantos termos voce quer mostrar? ')) 
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' Fim')