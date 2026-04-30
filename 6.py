def print_result(func):
    def wrapper(x):
        result = func(x)
        print(f"Result {func.__name__}({x}) = {result}")
        return result
    return wrapper
