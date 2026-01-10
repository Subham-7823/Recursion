#write a program that will print factorial of a number
def fact(num):
    if num == 0:
        return 1
    return num * fact(num-1)
print(fact(4))

"""

def factorial(num):
    if num>=0:
        if num == 0:
            return 1
        return  num * factorial(num-1)
    return "Invalid Number"
print(factorial(-1))

"""
