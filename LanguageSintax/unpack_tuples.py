# UNPACKING

nomes = ["Samuel", "Junior", "Arnaldo"]
nome1, nome2, nome3 = nomes 

"""
    OBS: Haverá um erro caso existam mais variáveis do que valores e vice-versa
    EX:
        nome1, nome2, nome3 = ["Jose", "Joao"] -> ERRO !
        nome1, nome2 = ["Jose", "Joao", "Joana"] -> ERRO !
"""
print(f"Nome 1: {nome1}\nNome 2: {nome2}\nNome 3: {nome3}")

materias = ["Matemática", "História", "Português"]

m1, *_ = materias
print(m1, _)

_, _, m3, *resto = materias
print(m3)

"""
    Quando queremos pegar um elemento específico de uma lista, podemos sinalizar as variáveis "inúteis" com "_", é uma convenção entre os especialistas em python.
    As variáveis "*_" e "*resto" declaradas, pegam todo o resto da lista, caso não haja mais o que pegar, elas serão listas vazias. 
"""

# TUPLAS

"""
Tipo tupla - Uma lista imutável
"""
nomes = ('Maria', 'Helena', 'Luiz')
# nomes = tuple(nomes)
# nomes = list(nomes)
print(nomes[-1])
print(nomes)
"""
Tipo tupla - Uma lista imutável
"""
nomes = ('Maria', 'Helena', 'Luiz')
# nomes = tuple(nomes)
# nomes = list(nomes)
print(nomes[-1])
print(nomes)