"""
https://www.geeksforgeeks.org/power-set/

Set  = [a,b,c]
power_set_size = pow(2, 3) = 8
Run for binary counter = 000 to 111

Value of Counter            Subset
    000                    -> Empty set
    001                    -> a
    010                    -> b
    011                    -> ab
    100                    -> c
    101                    -> ac
    110                    -> bc
    111                    -> abc
"""
import math

def powerset(arr, setSize):
    powerSetSize = (int)(math.pow(2, setSize))
    
    for counter in range(powerSetSize):
        for j in range(setSize):
            if counter & (1 << j):
                print(arr[j], end="")
        print()

arr = [1,2,3]
setSize = 3
powerset(arr, setSize)