# Time : O(n)
# Space : O(1)

def kadaneAlgorithm(array):
    maxEndingHere = array[0]
    maxSoFar = array[0]

    for item in array[1:]:
        maxEndingHere = max(item, maxEndingHere + item)
        maxSoFar = max(maxSoFar, maxEndingHere)

    return maxSoFar