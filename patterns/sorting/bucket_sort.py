"""
Bucket sort is mainly useful when input is uniformly distributed over a range. For example, consider the following problem. 
Sort a large set of floating point numbers which are in range from 0.0 to 1.0 and are uniformly distributed across the range. How do we sort the numbers efficiently?
A simple way is to apply a comparison based sorting algorithm. The lower bound for Comparison based sorting algorithm (Merge Sort, Heap Sort, Quick-Sort .. etc) is Ω(n Log n), i.e., they cannot do better than nLogn. 
Can we sort the array in linear time? Counting sort can not be applied here as we use keys as index in counting sort. Here keys are floating point numbers.  
The idea is to use bucket sort.
"""
import random
# Bucket sort is mainly used to sort decimal point numbers, although there is no point of using it anyway
# Suppose we only have decimal numbers with no integer
def bucketSortOnlyDecimals(arr):
    result = []
    slotNum = 10
    
    for i in range(10):
        result.append([])
        
    for item in arr:
        index = int(slotNum * item)
        result[index].append(item)
        
    for i in range(10):
        result[i].sort()
        
    output = []
    for element in result:
        output.extend(element)
        
    return output


# arr = [round(random.random(), 3) for _ in range(100)]
arr = [round(random.random(), 3) for _ in range(10)]
print(bucketSortOnlyDecimals(arr[:]))

# Bucket Sort with integers and decimals
# Exactly like above but with modification such as calculating range near the normalized value
def bucketSortHelper(arr, numberOfBuckets):
    result = []
    maxEle = max(arr)
    minEle = min(arr)
    rnge = (maxEle - minEle) / numberOfBuckets
    temp = []
    
    for _ in range(numberOfBuckets):
        temp.append([])
        
    for i in range(len(arr)):
        normal = ((arr[i] - minEle) / rnge) - ((arr[i] - minEle) // rnge)
        
        if normal == 0 and arr[i] != minEle:
            temp[int((arr[i] - minEle) // rnge) - 1].append(arr[i])
        else:
            temp[int((arr[i] - minEle) // rnge)].append(arr[i])
            
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()
            
    for element in temp:
        result.extend(element)
        
    return result

def bucketSort(arr):
    numberOfBuckets = len(set(arr))
    return bucketSortHelper(arr, numberOfBuckets)

print(bucketSort(arr[:]))
