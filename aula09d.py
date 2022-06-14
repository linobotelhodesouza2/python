'''
DESAFIO
CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NAO COM O NOME 'SANTO'
'''
cid = str(input('Digite o nome da cidade que voçê nasceu: ')).strip()# retira todos os espacos
print(cid[:5].upper() == 'SANTO') #pega a palavra santo joga tudo pra maiuscula e verifica se é igual a SANTO maiuscula

