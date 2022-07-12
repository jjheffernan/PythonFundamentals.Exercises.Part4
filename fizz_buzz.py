"""
Created by jj heffernan on 9 Jul 2022
fizz buzz example within Python 3
This is a very common test for interviews / whiteboarding
"""

for i in range(1, 100):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0 and i % 2 != 0:
        print('Fizz')
    else:
        print(i)
