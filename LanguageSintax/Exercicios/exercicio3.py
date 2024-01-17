# Exiba os indices da lista

lista = []
num_elementos = input("Numero de elementos: ")
num_elementos = int(num_elementos)

while num_elementos > 0:
    lista.append(input("Elemento: "))
    num_elementos -= 1

for elemento in lista:
    print(f"{lista.index(elemento)}: {elemento}")

