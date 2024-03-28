# Ordering people by age

def print_dict(list_):
    for people in list_:
        print(f'Name: {people['name']} - Last name: {people['last_name']} - Age: {people['age']}')

list_ = [
    {'name': 'Samuel', 'last_name': "Nunes", 'age': 20},
    {'name': 'Arnaldo', 'last_name': "Carvalho", 'age': 61},
    {'name': 'Ione', 'last_name': "Andrade", 'age': 48},
    {'name': 'Antonio', 'last_name': "Andrade", 'age': 49},
]

# Doing this: 

# def ordering(item):
#     return item['age']

# list_.sort(key = ordering)

# Is the same as doing this:

list_.sort(key = lambda item: item['age'])

print_dict(list_)