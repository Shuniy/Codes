# Time : O(n * target)
# Space : O(n)

def number_of_ways_coin_change(arr, target):
    # Additional
    arr.sort()

    number_of_ways = [0 for _ in range(target + 1)]
    number_of_ways[0] = 1
    
    for item in arr:
        for i in range(1, target + 1):
            if i >= item:
                number_of_ways[i] += number_of_ways[i - item]
    return number_of_ways_coin_change[-1]
