items = [ 0, None, 0.0, 1.0, True, 0, 7,]

found = False
for item in items:
    print("Scanning item", item)
    if item:
        found = True
        break

if found:
    print("At least one item evaluates to True")
else:
    print("All items evaluate to False")