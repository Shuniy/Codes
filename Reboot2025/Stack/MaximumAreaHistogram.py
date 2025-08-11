def NSR(arr):
    """
    Given an array `arr`, this function calculates the Next Smaller to Right (NSR) for each element in the array. It returns a list containing the indices of the next smaller element to the right for each element in the input array.
    """
    if not arr:
        return arr

    result = []
    stack = []

    for i, item in enumerate(reversed(arr)):
        if not stack:
            stack.append((item, len(arr) - i - 1))
            result.append(-1)
            continue

        while stack and stack[-1][0] >= item:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1][1])

        stack.append((item, len(arr) - i - 1))

    return list(reversed(result))


def NSL(arr):
    """
    Given an array 'arr', this function returns a list of the same length as 'arr', where each element at index 'i' represents the index of the Next Smaller Element (NSL) to the left of 'arr[i]'. If there is no smaller element to the left of 'arr[i]', the value at index 'i' will be -1.
    """
    if not arr:
        return arr

    result = []
    stack = []

    for i, item in enumerate(arr):
        if not stack:
            result.append(-1)
            stack.append((item, i))
            continue

        while stack and stack[-1][0] >= item:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1][1])

        stack.append((item, i))

    return result


def max_area_historgram(arr):
    """
    Calculate the maximum area of a histogram given an array of heights.

    Parameters:
    - arr: a list of integers representing the heights of the histogram bars

    Returns:
    - maxArea: an integer representing the maximum area of the histogram
    """
    if not arr:
        return arr

    left = NSL(arr)
    right = NSR(arr)

    max_area = float("-inf")
    for i, item in enumerate(arr):
        start = 0 if left[i] == -1 else left[i] + 1
        end = len(arr) - 1 if right[i] == -1 else right[i] - 1
        max_area = max(max_area, item * (end - start + 1))

    return max_area


# Driver program to test above function
arr = [1, 2, 1]
print(max_area_historgram(arr))
arr = [1, 2, 3, 4, 5]
print(max_area_historgram(arr))
arr = [5, 4, 3, 2, 1]
print(max_area_historgram(arr))
arr = [11, 13, 21, 3]
print(max_area_historgram(arr))
arr = [100, 80, 60, 70, 60, 75, 85]
print(max_area_historgram(arr))
arr = [1, 3, 2, 4]
print(max_area_historgram(arr))
arr = [1, 3, 0, 0, 1, 2, 4]
print(max_area_historgram(arr))
