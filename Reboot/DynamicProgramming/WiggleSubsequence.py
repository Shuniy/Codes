class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        return max(self.helper(nums, 0, False), self.helper(nums, 0, True))

    def helper(self, nums, index, isPrevPositive):
        if index >= len(nums) - 1:
            return 0
        output1 = float("-inf")
        output2 = float("-inf")
        if isPrevPositive:
            if nums[index + 1] < nums[index]:
                output1 = 1 + self.helper(nums, index + 1, False)
            else:
                output1 = self.helper(nums, index + 1, isPrevPositive)
        else:
            if nums[index + 1] > nums[index]:
                output2 = 1 + self.helper(nums, index + 1, True)
            else:
                output2 = self.helper(nums, index + 1, isPrevPositive)
        return max(output1, output2)

solution = Solution()
nums = [1, 7, 4, 9]
print(solution.wiggleMaxLength(nums))