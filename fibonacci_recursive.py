"""
Created by jj heffernan on 9 Jul 2022
playing with fibonacci sequence example within Python 3
This is a test for interviews / whiteboarding
"""
n = input("how far into fibonacci's sequence do you want to go?")
x = 1
def fibonacci():
    x = x
    y = x * (n-1) + x * (n - 2)
    return y
    fibonacci()
