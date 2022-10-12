'''
CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL
,NA ORDEM DE COLOCAÇÃO.DEPOIS MOSTRE:
A- OS 5 PRIMEIROS
B- OS ULTIMOS 4 COLOCADOS
C- TIMES EM ORDEM ALFABETICA
D- EM QUE POSIÇÃO ESTÁ O TIME DA CHAPECOENSE.
'''

print('--'* 154)
times = ('Palmeiras', 'Internacional', 'Corinthians', 'Flamengo', 'Fluminense', 'Athletico - PR', 'Atlético - MG',
         'América - MG', 'Botafogo', 'Fortaleza', 'Santos', 'São Paulo', 'Bragantino', 'Goiás', 'Coritiba', 'Ceará',
         'Cuiabá', 'Atlético - GO', 'Avaí', 'Juventude')
print(f'Lista de Times do Campeonato Brasileiro 2022 {times}')
print('--'* 154)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('--'* 154)
print(f'Os ultimos 4 colocados são: {times[16:]}')
print('--'* 154)
print(f'Times em Ordem Alfabética: {sorted(times)}')
print('--'* 154)
print(times[2])
print('--'* 154)
for pos, times in enumerate(times):
    print(f'Posição em que está o {times} {pos + 1}')
print('--'* 154)
