#write a program that will reverse a number
def reverse(num,sum=0):
    if num == 0:
        return sum
    sum = ((sum * 10) + (num % 10) ) 
    return reverse(num//10,sum)
print(reverse(14123))

#Note you can not assign to another varaible inside sum