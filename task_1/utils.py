
def fibonacci(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


fibonacci(3)  # 2
fibonacci(4)  # 3
fibonacci(0)  # 1
