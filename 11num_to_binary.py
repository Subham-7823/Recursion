#write a recursion program that will convert a number to binary
def binary(num,place=1):
    if num == 0:
        return 0
    return (num % 2)*place + binary(num//2,place*10)
num = 9
print(binary(num))