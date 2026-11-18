def NSL(arr):
    if not arr:
        return arr

    result = []
    stack = []

    for item in arr:
        if not stack:
            result.append(-1)
            stack.append(item)
            continue

        while stack and stack[-1] >= item:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(item)

    return result


# Driver program to test above function
arr = [11, 13, 21, 3]
print(NSL(arr))
arr = [1, 3, 2, 4]
print(NSL(arr))
arr = [1, 3, 0, 0, 1, 2, 4]
print(NSL(arr))
