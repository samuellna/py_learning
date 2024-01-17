"""
    Functions in python are piece of codes that get parameters and return a value. 
"""

import math

def soma(a = 0, b = 0):
    return a + b

def bhaskara(a = 0, b = 0, c = 0):
    delta = pow(b, 2) - 4 * a * c
    x1 = (b * (-1) + math.sqrt(delta)) / 2 * a
    x2 = (b * (-1) - math.sqrt(delta)) / 2 * a
    return (x1, x2)

option = input("There are two options:\n1 - Sum (a + b) \n2 - Bhaskara\n Type one of these numbers: ")

x = int(input("A = "))
y = int(input("B = "))

match int(option):
    case 1:
        sum_ = soma(x, y)
        print(f'{x = }, {y = } | x + y = {sum_}')
    case 2:
        z = int(input("C = "))
        result = bhaskara(x, y, z)
        print(f'Resultado = {result}')
    case default:
        print("Invalid option")
