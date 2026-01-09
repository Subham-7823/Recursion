#write a program that will take input from user and print even numbers in that range
def EvenNumber(start,end):
    if start==end+1:
        return
    if start % 2 == 0:
        print(start)
    EvenNumber(start+1,end)
EvenNumber(int(input("Enter starting number")),int(input("Enter ending number")))