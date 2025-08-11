def circular_array_loop_exists(arr: list[int]):
    for i, ele in enumerate(arr):
        is_forward = ele >= 0
        slow, fast = i, i

        while True:
            slow = find_next_index(arr, is_forward, slow)
            fast = find_next_index(arr, is_forward, fast)
            if fast != -1:
                fast = find_next_index(arr, is_forward, fast)

            if slow == -1 or fast == -1 or slow == fast:
                break
        if slow != -1 and slow == fast:
            return True

    return False

def find_next_index(arr: list[int], is_forward: bool, current_index: int):
    direction = arr[current_index] >= 0
    if direction != is_forward:
        return -1 # Change in direction
    
    next_index = (current_index + arr[current_index]) % len(arr)

    if current_index == next_index: 
        return -1 # one element cycle
    
    return next_index

def main():
    print(circular_array_loop_exists([1,2,-1,2,2]))
    print(circular_array_loop_exists([2,2,-1,2]))
    print(circular_array_loop_exists([2, 1, -1,-2]))

main()