'''
ESCREVA UM PROGRAMA PARA APROVAR O EMPRESTIMO BANCARIO PARA A COMPRA DE UMA CASA.O PROGRAMA VAI PERGUNTAR
O VALOR CASA, O SALARIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NAO PODE EXCEDER 30% DO SALARIO OU ENTAO O EMPRESTIMO
SERÁ NEGADO.
'''
casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite o valor do seu salário: '))
temp = int(input('Digite o tempo em anos para o pagamento do empréstimo: '))
prestMensal = (sal / 100) * 30# valor de 30 % do salário
anos = prestMensal * 12

valorMensal = (casa / temp) / 12# valor da prestação mensal do valor da casa

print('\nValor da casa: R${:.2f}\nSalario: R${:.2f}\nTempo de emprestimo: {} anos\n'
      'Valor mensal aprovado: R${:.2f}\nValor mensal das prestações: R${:.2f}\n'.format(casa, sal, temp, prestMensal, valorMensal))

if valorMensal > prestMensal:
    print('Empréstimo Negado')
elif valorMensal <= prestMensal:
    print('Empréstimo Aprovado')
