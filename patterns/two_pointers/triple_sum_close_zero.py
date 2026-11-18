def searchTriplet(arr: list[int], targetSum: int):
    arr.sort()
    smallestDifference = float("inf")
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            targetDiff = targetSum - arr[i] - arr[left] - arr[right]
            if targetDiff - targetSum == 0:
                return targetDiff - targetSum
            if abs(targetDiff) < abs(smallestDifference):
                smallestDifference = targetDiff
            if targetDiff > 0:
                left += 1
            else:
                right -= 1
    return targetSum - smallestDifference

def main():
    print(searchTriplet([-2, 0, 1, 2], 2))
    print(searchTriplet([-3, -1, 1, 2], 1))
    print(searchTriplet([1, 0, 1, 1], 100))

main()