from functools import wraps

def max_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if result > threshold:
                print(f"Result is too bit ({result})."
                      f"Max allowed is {threshold}."
                      )
                return max_result
            return wrapper
        return decorator
@max_result(75)
def cune(n):
    return n ** 3

print(cune(5))