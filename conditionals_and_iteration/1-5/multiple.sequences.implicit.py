people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23,24,23,21]
instruments = ['Drums', 'Keyboards', 'Bass', 'Guitar']
for data in zip(people, ages, instruments):
    person, age, instument = data
    print(person, age, instument)