#Another way to find prime number
def prime(num,val=2):
    if val == int(num**0.5)+1:
        return "Prime Number"
    if num % val == 0 and num<2:
        return "Not Prime Number"
    return prime(num,val+1)
num = 11
print(prime(num))