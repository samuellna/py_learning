import os

# Create a function that multiplies all not named arguments and returns it to a variable.
def mult(*args):
    num = 1
    for numbers in args:
        num *= numbers
    return num

# Create a function that return if the number is pair or odd
def pair_or_odd(number):
    return "Pair" if number % 2 == 0 else "Odd"

option = int(input("1 - Mult\n2 - Pair or Odd\nType one of these numbers: "))

match(option):
    case 1:
        numbers = []
        a = None
        while a != "Exit":
            a = input("Number: ")
            try:
                numbers.append(int(a))
            except:
                if a != "Exit":
                    print("That's not a number")
            os.system("cls")
        x = mult(*numbers)
        print(x)
        
    case 2:
        num = int(input("Number: "))
        result = pair_or_odd(num)
        print(num,"is", result)
    case default:
        print("Invalid option")

