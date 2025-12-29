import pprint

filmsDict = {
  "inception": {
    "yearRealease" : 2010,
    "imdbRating": 8.8,
    "genre": ["Sci-fi", "Action", "Thriller"]
  },
  "interstellar" :{
    "yearRealease" : 2010,
    "imdbRating": 8.8,
    "genre": ["Sci-fi", "Action", "Thriller"]
  },
  "the dark knight": {
    "yearRealease" : 2008,
    "imbRating": 9.0,
    "genre": ["Action", "Drama"]
  }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

#1 - Buscar uma informação dentro de um dicionario aninhado
print(filmsDict["interstellar"]["genre"])

# 2 - Adicionar novo item
filmsDict["inception"]["director"] = "Christopher Nolan"
print(["inception"])

# 3 - Excluir um dicionario
del filmsDict["the dark knight"]
pp.pprint(filmsDict)