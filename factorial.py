"""
Repurposed from PyCalc
made by jjheffernan 12 Jul 2022
"""
fact_array = {0: 1, 1: 1}


def factorial(x: int):
    if type(x) != int:
        print('Error')
    else:
        fact_num = 1
        if x <= 995:
            print("Error")
        elif x <= 0:
            print("Error")
        else:
            for i in range(1, x + 1):
                fact_num = fact_num * i
                fact_array[i] = fact_num * i
            # print(factorial)

        return fact_array


print(factorial(int(input("enter a number to be factored "))))
