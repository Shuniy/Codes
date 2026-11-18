def triplet_with_smaller_sum(arr: list[int], target_sum: int):
    arr.sort()
    result = []
    for i in range(len(arr) - 2):
        if i > 0 and arr[i - 1] == arr[i]:
            continue
        search_pair(arr, target_sum, i, result)
    return result

def search_pair(arr: list[int], target_sum: int, first: int, result: list[list[int]]):
    left = first + 1
    right = len(arr) - 1
    while left < right:
        if arr[first] + arr[left] + arr[right] < target_sum:
            for i in range(right, left, -1):
                result.append([arr[first], arr[left], arr[right]])
            left += 1
            while left < right and arr[left - 1] == arr[left]:
                left += 1
        else:
            right -= 1
            while left < right and arr[right + 1] == arr[right]:
                right -= 1

def main():
    print(triplet_with_smaller_sum([-1, -1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))

main()