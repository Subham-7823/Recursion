#write a python program that will take input from the user accroding
# to that it will print number
def print_number(start,end):
    if start == end+1:
        return
    print(start)
    print_number(start+1,end)
start = int(input("Enter starting number"))
end = int(input("Enter ending number"))
print_number(start,end)
    