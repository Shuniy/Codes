def search_quadruplets(arr: list[int], target_sum: int):
    arr.sort()
    quadruplets = []
    for i in range(len(arr) - 3):
        while i > 0 and arr[i - 1] == arr[i]:
            continue
        for j in range(i + 1, len(arr) - 2):
            if j > i + 1 and arr[j - 1] == arr[j]:
                continue
            search_pairs(arr, target_sum, i, j, quadruplets)
    return quadruplets

def search_pairs(arr: list[int], target_sum: int, first: int, second: int, quadruplets: list[int]):
    left = second + 1
    right = len(arr) - 1
    while left < right:
        s = arr[first] + arr[second] + arr[left] + arr[right]
        if s == target_sum:
            quadruplets.append([arr[first], arr[second], arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left - 1] == arr[left]:
                left += 1
            while left < right and arr[right + 1] == arr[right]:
                right -= 1
        elif s < target_sum:
            left += 1
        else:
            right -= 1

def main():
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))

main()