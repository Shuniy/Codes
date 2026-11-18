"""
Counting Inversions

Time Complexity: O(N log N)
Algorithmic Paradigm: Divide and Conquer
"""
def mergesort(arr, n): 

    temp_arr = [0]*n 
    return _mergesort(arr, temp_arr, 0, n-1) 
  
def _mergesort(arr, temp_arr, left, right): 
  
    inv_count = 0
    print("count " + str(inv_count))
  
    if left < right: 

        mid = (left + right)//2
  
        inv_count = _mergesort(arr, temp_arr, left, mid)
        print("count1 " + str(inv_count))
        inv_count += _mergesort(arr, temp_arr, mid + 1, right) 
        print("count2 " + str(inv_count))
  
        inv_count += merge(arr, temp_arr, left, mid, right) 
        print("count3 " + str(inv_count))
        
    return inv_count 
  
def merge(arr, temp_arr, left, mid, right): 
    i = left     
    j = mid + 1 
    k = left     
    inv_count = 0
  
    while i <= mid and j <= right: 
  
        if arr[i] <= arr[j]: 
            temp_arr[k] = arr[i] 
            k += 1
            i += 1
        else: 
            temp_arr[k] = arr[j] 
            inv_count += (mid-i + 1) 
            k += 1
            j += 1
  
    while i <= mid: 
        temp_arr[k] = arr[i] 
        k += 1
        i += 1
  
    while j <= right: 
        temp_arr[k] = arr[j] 
        k += 1
        j += 1
  
    for loop_var in range(left, right + 1): 
        arr[loop_var] = temp_arr[loop_var] 
          
    return inv_count

arr = list()
size = input("Enter array size : ")
print("Enter elements of array : ")
for i in range(int(size)):
    c = input()
    arr.append(int(c))
print("Entered array is : ")
print(arr)    

count = mergesort(arr, len(arr))

print("Inversion Count : ")
print(count)

print("Sorted array is : ")
print(arr, end = " ")