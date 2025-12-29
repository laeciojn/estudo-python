
filmInception = {
   # chaves são sempre únicas 
  "title" : "Inception",
  "yearRealease" : 2010,
  "imdbRating": 8.8,
  "genre": ["Sci-fi", "Action", "Thriller"]
}

print(filmInception)
print(len(filmInception))
print(type(filmInception))

# 1 - Recuperar um elemento do dicionario
print(filmInception["genre"])
print(filmInception.get("imdbRating"))

# 2 - Buscar apenas as chaves do dicionario
print(filmInception.keys())

# 3 - Buscar apenas os valores do dicionario
print(filmInception.values())

# 4 - Buscar itens do dicionario com chave e valor
print(filmInception.items())

# 5 - adicionar itens no dicionario
filmInception["director"] = "Christopher Nolan"
print(filmInception)

# 6 - Atualizar itens no dicionario
filmInception.update({"imdbRating ": 8.7})
print(filmInception)

# 7 - Remover o item do dicionario
filmInception.pop("director")
print(filmInception)