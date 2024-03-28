"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

import re # regular expression.
import sys

cpf = input("CPF (xxx.xxx.xxx-xx) : ")

# Transformando o CPF numa string numerica
cpf = re.sub(
    r'[^0-9]', # Tudo o que nao for um numero
    '', # Remova.
    cpf
)

rept_string = True if cpf.count(cpf[0]) == len(cpf) else False

if(rept_string):
    print("CPF inválido!")
    sys.exit()
    
fator = 11
num = 0
for digito in range(len(cpf)):
    if digito == len(cpf) - 1: break
    num += int(cpf[digito]) * fator
    fator -= 1
num *= 10
segundoDig = 0 if (num % 11 > 9) else (num % 11)
print(f'O segundo dígito é {segundoDig}')