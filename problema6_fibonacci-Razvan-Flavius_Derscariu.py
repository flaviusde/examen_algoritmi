# Problema 6 – Fibonacci recursiv (10p)

def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    print(fib(0))   # 0
    print(fib(1))   # 1
    print(fib(2))   # 1
    print(fib(3))   # 2
    print(fib(4))   # 3
    print(fib(5))   # 5
    print(fib(6))   # 8
    print(fib(10))  # 55