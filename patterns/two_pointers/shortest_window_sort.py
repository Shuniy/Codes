def shortest_window_sort(arr: list[int]):
    low = 0
    high = len(arr) - 1
    while low < len(arr) - 1 and arr[low] <= arr[low + 1]:
        low += 1
    
    if low == len(arr) - 1:
        return 0
    
    while high > 0 and arr[high] >= arr[high - 1]:
        high -= 1

    mn = float("inf")
    mx = float("-inf")
    for i in range(low, high + 1):
        mn = min(mn, arr[i])
        mx = max(mx, arr[i])

    while low > 0 and arr[low - 1] > mn:
        low -= 1
    
    while high < len(arr) - 1 and arr[high + 1] < mx:
        high += 1

    return high - low + 1

def main():
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))

main()