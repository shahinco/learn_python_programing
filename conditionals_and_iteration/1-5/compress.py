from itertools import compress
date = range(10)
even_selector = [1,0] * 10
odd_selector = [0,1] * 10

even_numbers = list(compress(date, even_selector))
odd_numbers = list(compress(date, odd_selector))

print(odd_selector)
print(list(date))
print(even_numbers)
print(odd_numbers)