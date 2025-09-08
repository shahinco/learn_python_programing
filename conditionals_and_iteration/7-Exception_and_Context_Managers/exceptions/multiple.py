values = (1,2)

try:
    q, r = divmod(*values)
except ZeroDivisionError:
    print("You tried to divide by Zero!")
except TypeError as e:
    print(e)