"""
Sort an array of 0,1 and 2

We can rearrange the array in single traversal using an alternative linear-time partition routine
can be used that seperates the values into three groups:

values less than the pivot
values equal to the pivot and
values greater than the pivot

"""

# we can count number of 0,1 and 2 and append at empty list

# consider 1 as a pivot

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def three_way_partition(arr, end):
    start = 0
    mid = 0
    pivot = 1

    while mid <= end:
        if arr[mid] < pivot:
            swap(arr, start, mid)
            start = start + 1
            mid = mid + 1
        elif arr[mid] > pivot:
            swap(arr, mid, end)
            end = end - 1
        else:
            mid = mid + 1

if __name__ == "__main__":
    arr = [0,1,2,2,1,0,0,2,0,1,1,0]
    three_way_partition(arr, len(arr) - 1)
    print(arr)