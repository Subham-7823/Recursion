#write a program to print prime number using recrsion
def prime(num,val=1):
    if val == num+1:
        return 0
    if num % val == 0:
        return 1 + prime(num,val+1)
    else:
        return prime(num,val+1)
num=7
if prime(num) == 2:
    print("Number is prime")
else:
    print("Number is not prime")