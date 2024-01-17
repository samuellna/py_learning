"""
    A única diferença de laços em python é o :
"""

nome = "Samuel Nunes"
nome_novo = ''
tamanho_nome = len(nome)
i = 0   

while i < tamanho_nome:
    nome_novo += f'*{nome[i]}'
    i += 1
print(nome_novo)