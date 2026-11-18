"""
Time Complexity: Sorting arrays on different machines. Merge Sort is a recursive 
algorithm and time complexity can be expressed as following recurrence relation.

T(n) = 2T(n/2) + \Theta(n)

The above recurrence can be solved either using Recurrence Tree method or 
Master method. It falls in case II of Master Method and solution of the 
recurrence is \Theta(nLogn).

Time complexity of Merge Sort is \Theta(nLogn) in all 3 cases 
(worst, average and best) as merge sort always divides the array into two halves 
and take linear time to merge two halves.

Auxiliary Space: O(n)

Algorithmic Paradigm: Divide and Conquer

Sorting In Place: No in a typical implementation

Stable: Yes

Applications of Merge Sort

Merge Sort is useful for sorting linked lists in O(nLogn) time.In the case of 
linked lists, the case is different mainly due to the difference in memory 
allocation of arrays and linked lists. Unlike arrays, linked list nodes may not 
be adjacent in memory. Unlike an array, in the linked list, we can insert items 
in the middle in O(1) extra space and O(1) time. Therefore merge operation of merge 
sort can be implemented without extra space for linked lists.

In arrays, we can do random access as elements are contiguous in memory. Let us 
say we have an integer (4-byte) array A and let the address of A[0] be x then to 
access A[i], we can directly access the memory at (x + i*4). Unlike arrays, we 
can not do random access in the linked list. Quick Sort requires a lot of this 
kind of access. In linked list to access i’th index, we have to travel each and 
every node from the head to i’th node as we don’t have a continuous block of memory. Therefore, the overhead increases for quicksort. Merge sort accesses data sequentially and the need of random access is low.

Inversion Count Problem
Used in External Sorting
"""
def mergesort(arr):
     if len(arr) > 1:
         mid = len(arr)//2
         left = arr[:mid]
         right = arr[mid:]
         print("left : " + str(left))
         print("right : " + str(right))
         
         mergesort(left)
         mergesort(right)
         print("left 1 : " + str(left))
         print("right 1 : " + str(right))
         
         i = j  = k = 0
         while i <len(left) and j < len(right):
             if left[i] <= right[j]:
                 arr[k] = left[i]
                 i += 1
             else:
                 arr[k] = right[j]
                 j += 1
             k += 1 
             
         while i < len(left):
              arr[k] = left[i]
              i = i+1
              k = k+1

         while j < len(right):
            arr[k] = right[j]
            j = j+1
            k = k+1    
        
array = list()
size = input("Enter array size : ")
print("Enter elements of array : ")
for i in range(int(size)):
    c = input()
    array.append(int(c))
print("Entered array is : ")
print(array)    

mergesort(array)

print("Sorted array is : ")
print(array, end = " ")
