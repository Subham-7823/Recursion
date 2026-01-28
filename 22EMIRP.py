# write a reursion function to check number is EMIRP number or not

#Number is not palindrome
#Number is prime
#Reverse number is also prime

def palindrome(num,sum=0):
    if num == 0:
        return sum
    return palindrome(num//10,((sum * 10 )+ (num % 10)))

def prime(num,val=2):
    if val == int(num**0.5):
        return True
    if num % val == 0:
        return False
    if num <= 1:
        return False
    return prime(num,val+1)

# def reverse_palindrome(palindrome(num,val=2)):
#      if val == int(num**0.5):
#         return True
#      if num % val == 0:
#         return False
#      if num <= 1:
#         return False
#      return prime(num,val+1)
#you cant do this
#you can not pass function call inside function defination

def EMIRP(num):
    rev = palindrome(num)
    if palindrome(num)!=num and prime(num) and prime(rev):
        return "NUmber is EMIRP number"
    return "Number is Not EMIRP number"

num = 113
print(EMIRP(num))
    
