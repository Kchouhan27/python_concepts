def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(5, 3)


#i am adding feature 1