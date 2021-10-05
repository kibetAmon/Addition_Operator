#a program that finds the sum power of numbers from
#one number to another

def sumnum(num1, num2,):
    addition = 0
    for i in range(num1, num2):
        k = i ** 2
        addition = addition + (i ** 2)
    return addition


def mainsum():
    a = 50
    b = 150
    k = 2
    print("Sum of power of numbers from 50 to 150 is: ", (k, a, b, sumnum(a, b,)))
    sumnum(50, 150)

mainsum()