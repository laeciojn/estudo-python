movieName = "Top Gun"

movieDescription = '''
  Top Gun Maverick é um filme de aviação e aventura
  muito consagrado na indústria
'''
print(movieName.upper())
print(movieName.lower())
print(movieName.capitalize()) #deixa a primeira letra em Maiúscula
print(movieName.title()) # deixa a primeira letra depois do espaço em Maiúscula
print(movieName.center(10, '-')) # retorna string centralizasa com caractere de preenchimento
print(movieName.find('u')) # retorna o indice do caractere passado
print(movieName.find("o")) # conta caracteres
print(movieName.replace("Top", "Matrix")) # altera elemento por outro
print(movieName.split(','))