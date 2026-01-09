#write a program that will check number is dizarum number or not
def dizarum(num,power):
    if num == 0:
        return 0
    return (num % 10)**power + dizarum(num // 10 , power-1)
num = int(input("Enter a number"))
power = len(str(num))
if num == dizarum(num,power):
    print("Number is dizarum number")
else:
    print("Number is not dizarum number")