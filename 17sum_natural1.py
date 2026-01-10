#Another way of sum of natural numbes
def natural(num):
    if num == 0:
        return 0
    return num + natural(num-1)
print(natural(3))