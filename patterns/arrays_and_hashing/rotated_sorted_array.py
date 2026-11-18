#You have to convert a sorted array in rotated array from a given position.

"""
a) Elements are first moved in first set
arr[] after this step --> {4 2 3 7 5 6 10 8 9 1 11 12}
b) Then in second set.
          arr[] after this step --> {4 5 3 7 8 6 10 11 9 1 2 12}
c) Finally in third set.
          arr[] after this step --> {4 5 6 7 8 9 10 11 12 1 2 3}
"""
#Finding Greatest common divisor
def GCD(a, b):
    if b == 0:
        return a
    else :
        return GCD(b, a%b)

#Juggling Theorem
def leftRotate(a, n, k) :
    k = k % n
    gcd = GCD(n, k)
    for i in range(gcd):
        temp = a[i]
        j = i
        d = (j + k) % n
        while 1:
            d = (j + k) % n
            if i == d:
                break
            a[j] = a[d]
            j = d
        a[j] = temp
    return a

#Reversal Theorem
def reverseArray(a, start, end):
    while start < end:
        temp = a[start]
        a[start] = a[end]
        a[end] = temp
        start += 1
        end -= 1

def leftRotate1(a, n, k):
    if k == 0:
        return
    reverseArray(a, 0, k - 1)
    reverseArray(a, k, n - 1)
    reverseArray(a, 0, n - 1)
    return a

#Reversal Theorem for right rotated sorted array
def rightRotate(a, n, k):
    if k == 0:
        return
    reverseArray(a, 0, n - 1)
    reverseArray(a, 0, k - 1)
    reverseArray(a, k, n - 1)
    return a

def printArray(a, n):
    for i in range (n):
        print ("%d" % a[i], end = " ")

a = [1, 2, 3, 4, 5, 6, 7]
n = len(a)
#leftRotate(a, 7, 2)
#leftRotate1(a, 7, 2)
rightRotate(a, 7, 2)
printArray(a, 7)
