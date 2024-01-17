#  CRUD: Create, Read, Update, Delete

person = {
    'name': 'Samuel',
    'last-name': 'Nunes',
    'age': '19',
    'address': [
        {'street': 'Claraval', 'number': '68'},
        {'street': 'Cin - UFPE', 'number': '66'}
    ],    
}

del person['last-name'] # Deleting a "key"
person['age'] = '20' # Updating the age

print(person)

cat = {}
cat['name'] = 'Loloca' # Dinamic creating

if cat.get('age', None):
    print("The cat doesn't have an reggistered age yet")

print(cat)