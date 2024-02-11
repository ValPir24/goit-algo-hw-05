def caching_fibonacci(n):
    cache = {}
    def fibonacci(n): # Function that calculates or returns fibonacci numbers
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache: # Checking if the number is already in cache
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci(n)

# Debugging
fib = caching_fibonacci
print(fib(10))
print(fib(15))
print(fib(20))