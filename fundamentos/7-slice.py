movieName = "Top Gun"

# string[inicio:fim] - indice começa na posição 0 | índice final -1

# 1 - Buscar toda string a partir da primeira posição
print(movieName[0:])

# 2 - Buscar toda string até a última posiçãoo
print(movieName[0:7])

# 3 - Buscar toda string até a 3 posição
print(movieName[2:])

"""
string[inicio:fim:passo] - 
indice começa na posição 0 | índice final -1
passo - determina o incremento. Por padrão esse número é o 1.
"""

# 4 - Buscar toda a String de 2 em 2
print(movieName[::2])

# 5 - Buscar toda a String nos indices impares
print(movieName[1:2])

# 6 - Inverter string de trás para frente
print(movieName[::-1])