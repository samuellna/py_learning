# Higher Order Functions receives a function (or functions) as an argument and return another function. T
# First-Class Functions - Functions that are treated like a basic variable type (int, string, ...) 

def sum__(*args):
    num = 0
    for numbers in args:
        num += numbers
    return num

def mult(*args):
    num = 1
    for numbers in args:
        num *= numbers
    return num
    
def execute_func(operation, *args):
    return operation(*args)

# execute = execute_func ----- This variable receives the function execute_func 

value = execute_func(sum__, 1, 2, 3, 4, 5, 100)
value2 = execute_func(mult, 12, 3, 2, 8)

print(value, value2)