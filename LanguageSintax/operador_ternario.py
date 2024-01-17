number = 9
new_number = number if number <= 9 else 0

print(number, new_number)

person = input("Name: ")
husband = "Junior" if (person == "Samuel" or person == "samuel") else "Unknowed"
print(f'{person}s husband is {husband}')