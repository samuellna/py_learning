import random

noveDigitos = ''
fator_1Digito = 10
fator_2Digito = 11
num = [0, 0] # Num é um vetor que armazena a soma dos nove digitos para calcular o 1o e segundo digito do CPF

for i in range(0, 9):
    noveDigitos += str(random.randint(0, 9)) # Armazenando um numero aleatorio entre 0 e 9
    
    # Calculando o primeiro e segundo dígito
    num[0] += int(noveDigitos[i]) * fator_1Digito
    num[1] += int(noveDigitos[i]) * fator_2Digito

    fator_1Digito -= 1
    fator_2Digito -= 1

primeiroDig = 0 if ((num[0] * 10) % 11) > 9 else ((num[0] * 10) % 11)

# Calculando o segundo dígito a partir do primeiro
num[1] += primeiroDig * fator_2Digito
segundoDig = 0 if ((num[1] * 10) % 11) > 9 else ((num[1] * 10) % 11)

cpf = noveDigitos + str(primeiroDig) + str(segundoDig)

print(f'O CPF gerado foi: {cpf}')