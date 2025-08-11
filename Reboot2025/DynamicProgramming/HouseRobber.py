class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        dp = nums.copy()
        dp.insert(0, 0)
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], (dp[i] + dp[i - 2]))
        return dp[-1]
