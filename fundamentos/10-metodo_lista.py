filmsList = ["Inception", "The Shawshank Redemption",
             "The Dark Kgnith", "Pulp Fiction", "Interstellar"]

# 1 - Tamanho da lista
print(len(filmsList))

# 2 - Recuperar um item da lista pelo índice
print(filmsList.index("Interstellar"))

# 3 adicionar um item ao final da lista
filmsList.append("The Lord of the Rings")
print(filmsList)

# 4 - Ordena lista
filmsList.sort()
print(filmsList)

# 5 - Copiar os itens de uma lista para outra
filmsCopy = filmsList.copy()
filmsCopy.remove("Pulp Fiction")
print(filmsCopy)

# 6 - Remove todos os itens da lista
filmsList.clear()
print(filmsList)
