# def func(a, b, c):
#     print(a, b, c)
#
# values = (1, 3, -7)
# func(*values)

my_list = [10, 20, 30]

def tricky_append(lst):
    lst.append(40)
    lst = [50, 60]
    lst.append(70)

tricky_append(my_list)
print(my_list)