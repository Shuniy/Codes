# Time : O(nlogn + mlogm)
# Space : O(1)

def smallestDifference(arr1, arr2):
    arr1.sort()
    arr2.sort()

    index1 = 0
    index2 = 0

    smallest = float("inf")

    current = float("inf")

    smallest_pair = []

    while index1 < len(arr1) and index2 < len(arr2):
        first_num = arr1[index1]
        second_num = arr2[index2]

        if first_num <= second_num:
            current = second_num = first_num
            index1 += 1
        elif second_num < first_num:
            current = first_num - second_num
            index2 += 1
        else:
            return [first_num, second_num]

        if smallest > current:
            smallest = current
            smallest_pair = [first_num, second_num]
    return smallest_pair
