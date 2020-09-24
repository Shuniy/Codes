# Time : O(n)/ Space O(1)
def findThreeLargestNumbers(array):
    three_largest = [None, None, None]
    for num in array:
        updateLargest(three_largest, num)
    return three_largest

def updateLargest(three_largest, num):
    if three_largest[2] is None or num > three_largest[2]:
        shift_and_update(three_largest, num, 2)
    elif three_largest[1] is None or num > three_largest[1]:
        shift_and_update(three_largest, num, 1)
    elif three_largest[0] is None or num > three_largest[0]:
        shift_and_update(three_largest, num, 0)

def shift_and_update(array, num, index):
    for i in range(index + 1):
        if i == index:
            array[i] = num
        else:
            array[i] = array[i + 1]