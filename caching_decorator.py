def cache(func):
    data = {}  # dictionary cache

    def wrapper(*args):
        if args in data:
            print("[CACHE] Returning cached result")
            return data[args]

        result = func(*args)
        data[args] = result
        return result

    return wrapper

@cache
def multiply(a, b):
    print("Calculating...")
    return a * b

print(multiply(3, 4))
print(multiply(3, 4))  # cached
