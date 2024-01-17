# Calculadora com while
sair = ""
while sair != 's':
    a = input("A: ")
    b = input("B: ")

    try:
        a = int(a)
        b = int(b)

        operacao = input("Operação: ")
        operadores = '%-+/*'
        if(operacao in operadores):
            if(operacao == '+'):
                print(f"{a} + {b} = {a + b}")
            elif(operacao == '-'):
                print(f"{a} - {b} = {a - b}")
            elif(operacao == '*'):
                print(f"{a} * {b} = {a * b}")
            elif(operacao == '/'):
                print(f"{a} / {b} = {a / b}")
            elif(operacao == '%'):
                print(f"{a} % {b} = {a % b}")
        else:
            print(f'{operacao} nao é um operador válido.')
        sair = input("Digite s para sair: ")
        sair = sair.lower()
    except:
        print("Digite um número válido.")