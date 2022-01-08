def get_next_index(current_index, arr):
    jump = arr[current_index]

    # If number/step greater than length of array
    next_index = (current_index + jump) % len(arr)
    
    # What if next index is negative, negative index works in python
    # but not in other languages
    return next_index if next_index >= 0 else next_index + len(arr)

def hasSingleCycle(arr):
    element_visited = 0

    current_index = 0 # Can be anything, choosing zero

    while element_visited < len(arr):
        if element_visited > 0 and current_index == 0:
            return False ## Dealing with multiple cycles
        element_visited += 1

        current_index = get_next_index(current_index, arr)
    return current_index == 0  