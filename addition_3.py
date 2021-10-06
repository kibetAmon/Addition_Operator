#a program that finds the sum power of numbers from
#one number to another

def sumnum(num1, num2, k):
    addition = 0
    for i in range(num1, num2):
        addition = addition + pow(i + 1, k)
    return addition


def mainsum():
    a = 50
    b = 150
    k = 2
    print("Sum of power of numbers from 50 to 150 is: ", (k, a, b, sumnum(a, b, k)))

mainsum()