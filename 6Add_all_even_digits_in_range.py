#write a program that will take staring and ending value from the user and print the sum of all 
#even number in that range

def EvenSum(start,end):
    if start == end+1:
        return 0
    if (start % 2 ) == 0:
        return start + EvenSum(start+1,end)
    else:
        return EvenSum(start+1,end)
print(EvenSum(int(input("Enter start number")),int(input("Enter end number"))))