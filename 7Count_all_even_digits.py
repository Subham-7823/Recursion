#write a program that will count all even digits present in a range
def count(num,end):
    if num == end+1:
        return 0
    return (num % 2 == 0) + count(num+1,end)
start = int(input("Enter starting number"))
end = int(input("Enter ending number"))
print(count(start,end))
