def fib(n: int)->int:
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
if __name__ == "__main__":
    print(fib(5))
    print(fib(10))
