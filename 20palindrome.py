#write a python program to check number is palindrome or not
def palindrome(num,sum=0):
    if num == 0:
        return sum
    return palindrome(num // 10 , ((sum * 10) + (num % 10)) )



number = int(input("Enter the number you want to check"))
if number == palindrome(number):
    print(f"{number} is palindrome")
else:
    print(f"{number} is not palindrome")