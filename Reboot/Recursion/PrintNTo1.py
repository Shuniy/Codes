def printNTo1(n):
    if n == 0:
        return
    print(n, end = " ")
    printNTo1(n - 1)

printNTo1(7)