a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaços? ', a.isspace())
print('È um número? ', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanúmerico?', a.isalnum())
print('È maiscula?', a.isupper())
print('É minuscula?', a.islower())
print('Está capitalizada?', a.istitle())
print('O tipo primitivo é {}, ele é {} de espaços, ele é um numero {}, ele é {} para alfabetico,ele é {} para alfanumerico, ele é {} para letras Maiúscula, ele é {} para letras Minúsculas, ele é {} para capilização'
      .format(type(a), a.isspace(), a.isnumeric(), a.isalpha(), a.isalnum(), a.isupper(), a.islower(), a.istitle()))






