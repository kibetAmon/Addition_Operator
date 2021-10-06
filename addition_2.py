# a program that returns the sum of numbers from number 1 to number 2
#by : amon

def sumnum(num1, num2):
    addition = 0
    for i in range(num1, num2):
        addition = addition + (i + 1)
    return addition


def mainsum():
    a = 50
    b = 150
    print("sum of numbers from 50 to 150 is: ", (a, b, sumnum(a, b)))

mainsum()