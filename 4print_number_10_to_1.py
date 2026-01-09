def Ten2one (num):
    if num == 0:
        return
    print(num)
    Ten2one(num-1)
Ten2one(10)