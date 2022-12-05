# time : O(n^2), space : O(1)
def two_number_sum(arr, target):
    for i in range(len(arr) - 1):
        firstnum = arr[i]
        for j in range(i + 1, len(arr)):
            secondnum = arr[j]
            if secondnum + firstnum == target:
                return (firstnum, secondnum)
    return []

# time : O(n), space : O(n)
def hash_two_number(arr, target):
    hashmap = {}
    for i, item in enumerate(arr):
        if target - item in hashmap:
            return (target - item, item)
        else:
            hashmap[item] = i

# time : O(nlogn), space : O(1)
def sort_two_number(arr, target):
    arr.sort()
    i = 0
    j = len(arr) - 1

    while i < j:
        if arr[i] + arr[j] == target:
            return (arr[i], arr[j])
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            j -= 1
    return []

if __name__ == "__main__":
    arr = [3, 5, -4, 8, 11, -1, 6]
    target = 10
    two_number_sum(arr, target)
