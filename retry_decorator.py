import random
import time

def retry(times=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[RETRY] Attempt {attempt} failed: {e}")
                    time.sleep(0.5)
            raise Exception(f"{func.__name__} failed after {times} retries")
        return wrapper
    return decorator

@retry(times=3)
def unstable():
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success!"

print(unstable())

#git pull example

