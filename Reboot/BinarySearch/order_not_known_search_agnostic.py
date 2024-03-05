def order_not_known_search_agnostic(arr, target):
    left = 0
    right = len(arr) - 1
    
    # 0 for ascending, 1 for descending
    order = 0 if arr[left] < arr[right] else 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            if order == 0:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if order == 0:
                left = mid - 1
            else:
                right = mid + 1
                
    return -1

# test cases for above function
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
print(order_not_known_search_agnostic(arr, target))   
arr = [9,8,7,6,5,4,3,2,1,0]
target = 7
print(order_not_known_search_agnostic(arr, target))   
