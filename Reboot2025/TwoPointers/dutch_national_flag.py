def dutch_flag_sort(arr: list[int]):
    # it is simple, get two pointers, put all 0's before 1st pointer
    # and put all 2s after second pointer
    low = 0 # put 0 here
    high = len(arr) - 1 # put 2 here
    i = 0 # i pointer is the pointer to put 1
    # basically its simple low is the place where 0 will be or the leftmost place
    # before i pointer
    # and high is the place where 2 will be or the rightmost place after i pointer
    # and just keep switching with 1 pointer place with low and high
    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1

def main():
    arr = [1,0,2,1,0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)

main()