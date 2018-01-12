#!/usr/bin/env python3
# this introduces recursive fibonacci with a cache of recent function calls
# this is introducing memoization: caching recent function call results

fibonacci_cache = {}


def fibonacci(n):
    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    fibonacci_cache[n] = value
    return value


for n in range(1, 101):
    print(n, ":", fibonacci(n))

