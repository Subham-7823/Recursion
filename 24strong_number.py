#write a python program to check number is strong number or not
# num = 145
# 1! = 1
# 4! = 24
# 5! = 120
# Total = 1 + 24 + 120 = 145

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num-1)

def digit(num):
    if num == 0:
        return 0
    return factorial(num % 10) + digit(num//10)

def strong(num):
    if digit(num) == num:
        return "Number is strong number"
    return "Number is not strong number"

num = 145
print(strong(num))