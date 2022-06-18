#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 01:31:47 2022

@author: lino
"""

from random import randint
from time import sleep
comp = randint(0, 5) #isso faz com que o numerador fique sempre mudando 
print('---'*10)
print('Vou pensar em um numero entre 0 e 5  tente adivinhar..')
print('---'*10)
jg = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jg == comp:
    print('Parabens!Voce conseguiu me vencer')
else:
    print('Ganhei! Pensei no numero {} e nao no numero {}'.format(comp, jg))
    