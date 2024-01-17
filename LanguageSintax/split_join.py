"""
    split - divides a str with a given character
    join - combines strings 
"""

frase = "My name is samuel and i love my boyfriend"
list_words = frase.split() # If there'snt an argument given, .split() will return a list of substrings, each substring will be separated by spaces.
print(list_words) # ['My', 'name', 'is', 'samuel', 'and', 'i', 'love', 'my', 'boyfriend']

another_list = frase.split('a') # The argument won't be in the list.
print(another_list)

frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)