#write a recrsion function to to check number is palyprime or not
#if number is palindrome and prime then it is known as palyprime

def palindrome(num,sum=0):
    if num == 0:
        return sum
    return palindrome(num //10,sum*10+num%10)


def prime(num,val=2):
    if num <= 1:
        return False
    if val == int(num**0.5) +1:
      return True
    if num % val == 0:
        return False
    return prime(num,val+1)

def palyprime(num):
    if palindrome(num)==num and prime(num):
        return "palyprime"
    return "Not Palyprime"

num = 372
print(palyprime(num))
    