"""
Created by jj heffernan on 9 Jul 2022
playing with fibonacci sequence example within Python 3
This is a test for interviews / whiteboarding
"""

# n = 0
# x = 1
fib_Array = {0: 0, 1: 1}  # declare dictionary
# this done to avoid going into negative ints


def fibonacci(n):
    # removed due to not properly implementing recursion
    # if n <= 2:
    #     print(1)
    # else:
    #     y = x * (n - 1) + x * (n - 2)
    #     return y
    if n in fib_Array:
        # print(f"{n} is not a correct input ")
        return fib_Array[n]
    # elif n == 1 or n == 2:
        # return 0
        # print(n)
    # else:
    fib_Array[n] = fibonacci(n-1) + fibonacci(n-2)

    return fib_Array[n]


# error case escape
print(fibonacci(int(input('How far into fibonacci do you want to go? '))))
print(fib_Array)
# removed, see above on line 12
# if 0 <= n: int(input("start fib "))
#     n = input("how far into fibonacci's sequence do you want to go? ")
# else:
#     for i in range(n):
#         print(f"| n = \t | {n} | \n | x(n) = \t | {fibonacci(i)} |")
