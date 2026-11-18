def cycle_sort(nums: list[int]):
	i = 0
	while i < len(nums):
		val = nums[i]
		if val != i + 1:
			nums[val - 1], nums[i] = nums[i], nums[val - 1]
		else: 
			i += 1
	return nums

def main():
	print(cycle_sort([3, 1, 5, 4, 2]))
	print(cycle_sort([2, 6, 4, 3, 1, 5]))
	print(cycle_sort([1, 5, 6, 4, 3, 2]))

main()
