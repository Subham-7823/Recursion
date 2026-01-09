#write a program that will take a number and add all digits of number
def add(num):
    if num == 0:
        return 0
    return (num % 10) + add(num//10)
num = 123
print(add(num))