flavors = ["pistachio", "mango", "vanilla", "chocolate", " strawberry", "banana"]
prompt = "Choose your flavor: "
print(flavors)
while (choice := input(prompt)) not in flavors:
    print(f"Sorry '{choice}' is not a valid option.")
print(f"You chose '{choice}'.")