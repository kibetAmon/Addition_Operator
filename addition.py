#a program that finds the sum of numbers from 1 to 100

def sumnum():
    addition = 0
    for i in range(1, 101):
        addition = addition + i
    return addition

print("The sum of numbers from 1 to 100 = ", sumnum())
