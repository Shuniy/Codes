"""
What is the running time of Radix Sort?
Let there be d digits in input integers. Radix Sort takes O(d*(n+b)) time where b is 
the base for representing numbers, for example, for decimal system, b is 10. What is 
the value of d? If k is the maximum possible value, then d would be O(logb(k)). So 
overall time complexity is O((n+b) * logb(k)). Which looks more than the time 
complexity of comparison based sorting algorithms for a large k. Let us first 
limit k. Let k <= nc where c is a constant. In that case, the complexity becomes 
O(nLogb(n)). But it still doesn’t beat comparison based sorting algorithms.

What if we make value of b larger?. What should be the value of b to make the time 
complexity linear? If we set b as n, we get the time complexity as O(n). In other 
words, we can sort an array of integers with range from 1 to nc if the numbers are 
represented in base n (or every digit takes log2(n) bits).

Is Radix Sort preferable to Comparison based sorting algorithms like Quick-Sort?
If we have log2n bits for every digit, the running time of Radix appears to be 
better than Quick Sort for a wide range of input numbers. The constant factors 
hidden in asymptotic notation are higher for Radix Sort and Quick-Sort uses hardware 
caches more effectively. Also, Radix sort uses counting sort as a subroutine and 
counting sort takes extra space to sort numbers.
"""

def countingsort(arr, exp1): 
    n = len(arr)   
    output = [0] * (n)  
    count = [0] * (10) 
  
    for i in range(0, n): 
        index = int((arr[i]/exp1)) 
        count[ (index)%10 ] += 1
  
    for i in range(1, 10): 
        count[i] += count[i-1] 
  
    i = n-1
    while i >= 0: 
        index = int((arr[i] / exp1)) 
        output[ count[ (index) % 10 ] - 1] = arr[i] 
        count[ (index) % 10 ] -= 1
        i -= 1
        
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
  
def radixsort(arr): 
    max1 = max(arr) 
    exp = 1
    while max1 / exp > 0: 
        countingsort(arr,exp) 
        exp *= 10    
    
    
arr = list()
size = input("Enter size of the array : ")

print("Enter elements of array : ")
for i in range(int(size)):
    c = input()
    arr.append(int(c))
    
print("Entered array is : ")
print(arr)

radixsort(arr)

print("Sorted array is : ")
print(arr)      