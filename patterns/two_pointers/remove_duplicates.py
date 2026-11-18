def remove_duplicates(arr):
    next_non_duplicate = 1
    i = 1
    while i < len(arr):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate], arr[i] = arr[i], arr[next_non_duplicate]
            next_non_duplicate += 1
        i += 1
    return next_non_duplicate

def main():
    arr = [2,3,3,3,6,9,9]
    print(remove_duplicates(arr), arr)
    arr = [2,2,2,11]
    print(remove_duplicates(arr), arr)

main()