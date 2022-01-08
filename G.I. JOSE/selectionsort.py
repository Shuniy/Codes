"""
Time Complexity: O(n^2) as there are two nested loops.

Auxiliary Space: O(1)
The good thing about selection sort is it never makes more than O(n) swaps and 
can be useful when memory write is a costly operation.

Stability : The default implementation is not stable. However it can be made stable. Please see stable selection sort for details.

In Place : Yes, it does not require extra space.
"""

def selectionsort(arr):
    
    for i in range(len(arr)):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
                
        arr[i], arr[mini] = arr[mini], arr[i]
        
arr = list()
size = input("Enter size of the array : ")

print("Enter elements of array : ")
for i in range(int(size)):
    c = input()
    arr.append(int(c))
    
print("Entered array is : ")
print(arr)

selectionsort(arr)

print("Sorted array is : ")
print(arr)        
            
        
    