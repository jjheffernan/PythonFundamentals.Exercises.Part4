"""
ported over from original build of fibonacci recursive, that wasnt so recursive
made by jjh on 13 Jul 2022
"""

fib_Array = {0: 0, 1: 1}  # declare dictionary
# this done to avoid going into negative ints


def fibonacci(n):
    # n = 0
    x = 0
    y = 1
    z = 0

    if n in fib_Array:
        # print(f"{n} is not a correct input ")
        return fib_Array[n]
    else:
        for i in range(2, n+1):
            z = x + y
            x = y
            y = z
            fib_Array[i] = z

    # elif n == 1 or n == 2:
        # return 0
        # print(n)
    # else:
    # fib_Array[n] = fibonacci(n-1) + fibonacci(n-2)

    return fib_Array


# error case escape
fibonacci(int(input('How far into fibonacci do you want to go? ')))
print(fib_Array)

