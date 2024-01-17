"""
    try -> tentar executar o código
    except -> ocorreu um erro ao tentar executar
"""

# Exemplo: 
numero = input("Vou dobrar o numero que você digitar: ")

try:
    numero_int = int(numero)
    print(f"INT: {numero_int}")
    print(f"O dobro de {numero} é {numero_int * 2}") # Se usar uma operação do tipo str * n, onde n é um numero, a string será repetida n vezes.
except:
    print("Isso não é um número.")
