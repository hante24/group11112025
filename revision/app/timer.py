import datetime
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()

        result = func(*args, **kwargs)

        end_time = datetime.datetime.now()
        elapsed_time = (end_time - start_time).total_seconds()

        print(f"{func.__name__} took {elapsed_time:.3f} seconds")

        return result

    return wrapper