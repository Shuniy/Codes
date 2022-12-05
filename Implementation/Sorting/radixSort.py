# Time : O()
import random


# Time Complexity : O(n + b)
# Space : O(n)
def radixSortHelper(arr, expo):

    n = len(arr)

    bitSorted = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = arr[i] // expo
        count[index % 10] += 1

    # Here, we are calculating the positions of the elements,
    # let arr = [3,33,333,3333,2,22,1,11,111,1111,0,10]
    # for examples, count = [2,4,2,4] -> this means that, we have,
    # two elements whose last bit ends with 0
    # four elements whose last bit ends with 1
    # two elements whose last bit ends with 2
    # four elements whose last bit ends with 3
    # and suppose we are in first iteration that is expo = 1
    # we want our output array to be in way such that all elements whose last bit ends with 0
    # and then rest of the elements in same way
    # we want output to be = [0, 10(all elements with 0), 1,11,111,1111 (all elements with 1) and so on... ]
    # doing below operation will make count array as -> [2,6,8,12]
    # above count means, elements with 0 will be inserted in indexes (0,1)
    # and elements with 1 will be inserted in indexes (0, 6) but we have 4 elements so, will be inserted between (2,6),
    # and rest of the elements will be inserted in same way, therefore, we will traverse the arr in reverse order
    # and insert the elements in reverse order in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // expo
        bitSorted[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(n):
        arr[i] = bitSorted[i]

# MIT radix sort
# https://www.youtube.com/watch?v=Nz1KZXbghj8
# Time : O((n + b) * d) // d = maxPlaces = logb(k)


def radixSort(arr):

    maxPlaces = max(arr)

    expo = 1
    while maxPlaces // expo > 1:
        radixSortHelper(arr, expo)
        expo *= 10


arr = [random.randint(1, 9999) for _ in range(100)]
# arr = [9,8,7,6,5,4,3,2,1,0,11,99,88,77,66,55,44,33,22,100,101,34,1111,23]
radixSort(arr)
print(arr)
