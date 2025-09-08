items = 'ABCD'
paris = []

for a in range(len(items)):
    for b in range(a, len(items)):
        paris.append((items[a], items[b]))
        