frase = "O rato comeu"

i = 0
mais_rept = 0   
letra_mais_rept = ''

while i < len(frase):
    if(frase[i] != ' '):
        letra_atual = frase[i]
        rept = frase.lower().count(letra_atual)
        if(mais_rept < rept):
            mais_rept = rept
            letra_mais_rept = letra_atual
    i += 1

print(f'A letra mais repetida foi: {letra_mais_rept}, repetindo-se {mais_rept}x')
