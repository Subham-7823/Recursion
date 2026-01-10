#write a program that will used to reverse number
#and dont use another line to store it in a variable
def reverse(num,sum=0):
    if num == 0:
        return sum
    return reverse(num//10 , ((sum*10)+(num%10)))
print(reverse(143))

#THE difference in previous program and this program is
#previous the result we are storing  in a variable and that is passed inside the function
#here that operation directly done inside the function argument
#so that first that logic is executed then will generate a number and that number is passed as function argument