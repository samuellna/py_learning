def create_multiplier(num = 1):
    def mult_x(factor = 1):
        return num * factor
    return mult_x

number = int(input("Number: "))
value = create_multiplier(number)

print(value(2), value(3), value(4))