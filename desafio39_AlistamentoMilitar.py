'''
FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME , DE ACORDO COM SUA IDADE:
- SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR.
- SE É A HORA DE SE ALISTAR;
- SE JÁ PASSOU DO TEMPO DO ALISTAMENTO
 SEU PROGRAMA TAMBEMM DEVERA MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO.
'''
from datetime import date# importa a biblioteca de data e o import date a data especifica no caso today hoje
nasc = int(input('Digite o ano de Nascimento: '))
today = date.today().year# especifica que eu quero somente o ano .year
idade = today - nasc
alist = 17

if idade == alist:
    print('Olá, voçê tem {} anos, e esta no periodo de alistamento militar, procure uma agência e se aliste.'.format(idade))
elif idade > alist:
    print('Olá, voçê tem {} anos e ja passou do periodo de alistamento militar em {} anos,\n'
          'procure uma agência para regularizar sua situação.'.format(idade, idade - alist))
elif idade < alist:
    print('Olá, voçê tem {} anos e falta {} anos ainda, não esta no periodo de alistamento militar,\n'
          'mais esta próximo.'.format(idade, alist - idade))