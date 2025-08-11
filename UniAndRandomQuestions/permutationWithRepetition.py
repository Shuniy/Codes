"""
All we have to do is keep track of index and when reaches the n
store it
"""


def permutationWithRepetitionHelper(arr, currentIndex, n, hashmap):

    for i in range(n):
        hashmap[currentIndex] = arr[i]
        if currentIndex == n - 1:
            result.append(hashmap[:])
        else:
            permutationWithRepetitionHelper(arr, currentIndex + 1, n, hashmap)


def permutationWithRepetition(arr, n):
    permutationWithRepetitionHelper(arr, 0, n, [None for _ in range(n)])


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.permuteHelper(nums, [], result)
        return result

    def permuteHelper(self, nums, current, result):
        if len(current) == len(nums):
            result.append(current[:])
            return

        for item in nums:
            current.append(item)
            self.permuteHelper(nums, current, result)
            current.pop()


arr = [1, 2, 3]
result = []
n = len(arr)
permutationWithRepetition(arr, n)
print(result)
