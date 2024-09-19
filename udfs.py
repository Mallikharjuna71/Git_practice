def decorator(func):
    def wrapper(a, b):
        k = func(a, b)
        k = k*2
        return k
    return wrapper

@decorator
def sm(a, b):
    return a+b

print(sm(1, 5))