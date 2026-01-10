#write a python program to print sum of n natural numbers
def natural(num,start=1,sum=0):
    if num>0:
        if start == num+1:
            return sum
        return natural(num,start+1,(sum+start))
print(natural(5))



