#!/usr/bin/env python3
# this shows the fibonacci sequence with basic recursion.
# note that it gets very slow at the end due to the recursion


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


for n in range(1, 101):
    print(n, ":", fibonacci(n))
