#write a python program that will convet mnumber to binary to integer
def Int_to_binary(num,place=0):
    if num  == 0:
        return 0
    return (num % 10) * (2**place) + Int_to_binary(num // 10 ,place+1)
print(Int_to_binary(1001))