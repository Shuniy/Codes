# Time : O(n)/ Space O(1)
def findThreeLargestNumbers(array):
    three_largest = [None, None, None]
    for num in array:
        three_largest = updateLargest(three_largest, num)
    return three_largest

def updateLargest(three_largest, num):
    if three_largest[2] is None or num > three_largest[2]:
        three_largest = shift_and_update(three_largest, num, 2)
    elif three_largest[1] is None or num > three_largest[1]:
        three_largest = shift_and_update(three_largest, num, 2)
    elif three_largest[0] is None or num > three_largest[0]:
        three_largest = shift_and_update(three_largest, num, 2)

    return three_largest

def shift_and_update(three_largest, num, index):
    for i in range(index + 1):
        if i == index:
            three_largest[i] = num
        else:
            three_largest[i] = three_largest[i + 1]
    return three_largest

arr = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

three = findThreeLargestNumbers(arr)
print(three)
