#write a recrsive function to check number is facinating number or not
def facinate_number(num,val=1):
    if val==10:
        return "Facinating number"
    if num.count(str(val))!=1:
        return "Not Facinating number"
    return facinate_number(num,val+1)
num=250
number = str(num) + str(num*2) + str(num*3)
print(facinate_number(number))