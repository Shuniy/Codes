class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        ans = self.minOperationsHelper(nums, 0, n - 1, x)
        return ans if ans != float("inf") else -1

    def minOperationsHelper(self, nums, left, right, target):
        if left >= right:
            return float("inf")
        if target == 0:
            return 0
        output1 = 1 + self.minOperationsHelper(
            nums, left + 1, right, target - nums[left])
        output2 = 1 + self.minOperationsHelper(
            nums, left, right - 1, target - nums[right])
        return min(output1, output2)

solution = Solution()
arr = [1,1,4,2,3]
target = 5
print(f"Minimum Operations are: {solution.minOperations(arr, target)}")