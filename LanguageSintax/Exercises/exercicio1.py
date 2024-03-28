opcao = input("Qual exercicio veyr? ")

if(opcao == '1'):
    # 1)
    numero = input("// Digita um (numero) inteiro veyr: ")

    try:
        numero = int(numero)
        if(numero % 2 == 0):
            print(f"{numero} é par veyr!")
        else:
            print(f"{numero} é ímpar veyr!")
    except:
        print("// Tu não digitou um número inteiro veyr, nojo realr!")
elif(opcao == '2'):
    # 2)
    hora = input("// Que horas são veyr (formato 24h mor)? ")
    
    try:
        hora = int(hora[0: 2: 1])
        if(hora <= 11 and hora >= 0):
            print("Bom dia veyr! ")
        elif(hora <= 17 and hora >= 12):
            print("Boa tarde veyr!")
        elif(hora >= 18 and hora <= 23):
            print("Boa noite veyr!")
    except:
        print("// Tu não digitou as horas certo veyr, nojo realr!")
else:
    nome = input("// (Qual) o teu nome veyr? ")
    tamanho_nome = len(nome)


    if tamanho_nome >= 1:
        if(tamanho_nome <= 4): 
            print("// Teu nome é (muito curto) veyr!")
        elif(tamanho_nome >= 5 and tamanho_nome <= 6): 
            print("// Teu nome é (normal) veyr!")
        else: 
            print("// Teu nome é (muito grande) veyr!")
    else:
        print("Digita algo veyr!")