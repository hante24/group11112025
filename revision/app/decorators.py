def round_result(ndigits: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if isinstance(result, (int, float)):
                return round(result, ndigits)

            return result
        return wrapper
    return decorator