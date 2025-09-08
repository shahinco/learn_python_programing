from time import time
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t =time()
        result = func(*args, **kwargs)
        print(func.__name__, 'took:', time() -t)
        return result

    def max_result(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > 100:
                print(
                    f'Restult is too big ({result}).'
                    'Max allowed is 100.'
                )
            return result
        return wrapper

@measure
@max_result
def cube(n):
    return n ** 3

print(cube(2))
print(cube(5))