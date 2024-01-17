"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""


lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a # Basicamente, lista_b aponta para o mesmo end. de memória de lista_a, portanto, se alterarmos o valor de lista_a, alteraremos o de lista_b.
lista_c = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
print(lista_c) # Porém, ao usarmos o método .copy(), a lista_c recebe o mesmo valor de lista_a, mas não aponta para o mesmo lugar na memória, logo, se mudarmos lista_a, não mudamos lista_c

# for in com listas
lista = [10, 20, 30, 40, 50]
for numero in lista:
    print(numero, type(numero))