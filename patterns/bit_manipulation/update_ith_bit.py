def updateithbit(n, i, val):
    # clear the ith bit
    num = n & (~(1 << i))
    # then do or with the val shifted to that
    return num | (val << i)

n = 5
i = 2
val = 1
print(updateithbit(n, i, val))
