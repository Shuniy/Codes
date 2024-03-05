def stock_span_problem(arr):
    """
    Calculate the stock span for each element in the given array.

    Parameters:
    arr (list): The input array of stock prices.

    Returns:
    list: A list of integers representing the stock span for each element in the input array.
    """
    if not arr:
        return arr

    result = []
    ngl_indexes = []
    stack = []
    for i, item in enumerate(arr):
        if not stack:
            stack.append((item, i))
            ngl_indexes.append((item, -1))
            continue
        while stack and stack[-1][0] <= item:
            stack.pop()

        if not stack:
            ngl_indexes.append((item, -1))
        else:
            ngl_indexes.append(stack[-1])
        stack.append((item, i))

    for i, item in enumerate(ngl_indexes):
        if item[1] == -1:
            result.append(-1)
        else:
            result.append(i - item[1])

    return result


# Driver program to test above function
arr = [11, 13, 21, 3]
print(stock_span_problem(arr))
arr = [100, 80, 60, 70, 60, 75, 85]
print(stock_span_problem(arr))
arr = [1, 3, 2, 4]
print(stock_span_problem(arr))
arr = [1, 3, 0, 0, 1, 2, 4]
print(stock_span_problem(arr))
