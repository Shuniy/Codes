"""
Problem Name: Median of Sorted Arrays

Problem Difficulty: None

Problem Constraints: N < 1000
Problem Description:

We are given two sorted arrays of same size n. 
Find the median of an array formed after merging these two sorted arrays.

Input Format: First line contains the input n. 
Second and Third line contains n space separated integers.

Sample Input: 5
1 3 5 7 9
2 4 6 8 10

Output Format: Print the median in a single line.
Sample Output: 5

"""

def find_median_sorted_array(arr: list[list[int]]):
	# time: O(log(min(m,n)))
	nums1 = arr[0]
	nums2 = arr[1]
	m = len(nums1)
	n = len(nums2)

	if m > n:
		nums1, nums2, m, n = nums2, nums1, n, m

	start = 0
	end = m - 1
	half_length = (n + m) // 2
	# All i need a partition such that all the smaller elements are on left side
	# and all the bigger elements are on right
	# Since, each array is sorted, we have to compare the left and right of each other
	# with the other one, means ALeft <= BRight and ARight >= BLeft
	# To get this marker, we will use pointers or partition marker element to represent split
	while True:
		partitionNums1 = (start + end) // 2
		partitionNums2 = half_length - partitionNums1 - 1
		nums1Left = nums1[partitionNums1] if partitionNums1 >= 0 else float("-inf")
		nums1Right = nums1[partitionNums1 + 1] if partitionNums1 < m else float("inf")
		nums2Left = nums2[partitionNums2] if partitionNums2 >= 0 else float("-inf")
		nums2Right = nums2[partitionNums2 + 1] if partitionNums2 < n else float("inf")

		if nums1Left <= nums2Right and nums1Right >= nums2Left:
			# correct partition
			if (n + m) % 2:
				# odd
				return min(nums1Right, nums2Right)
			else:
				return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2
			
		elif nums1Left > nums2Right:
			end = partitionNums1 - 1
		else:
			start = partitionNums1 + 1

	return -1


def find_median_sorted_array_sorted(arr: list[list[int]]):
	nums1 = arr[0]
	nums2 = arr[1]
	arr = []
	i = 0
	j = 0
	while i < len(nums1) and j < len(nums2):
		if nums1[i] <= nums2[j]:
			arr.append(nums1[i])
			i += 1
		else:
			arr.append(nums2[j])
			j += 1
	while  i < len(nums1):
		arr.append(nums1[i])
		i += 1
	while  j < len(nums2):
		arr.append(nums2[j])
		j += 1
	n = len(arr) // 2
	return arr[n] if len(arr) % 2 else (arr[n] + arr[n - 1]) / 2

def main():
	arr = []
	for i in range(1, 3):
		size = int(input("Enter size of each arrays: "))
		print(f"Enter {i}th array: ")
		temp = []
		for j in range(size):
			temp.append(int(input(f"Enter {j}th element: ")))
		arr.append(temp)

	print("Median of the arrays is: ", find_median_sorted_array_sorted(arr))
	print("Median of the arrays is: ", find_median_sorted_array(arr))

main()
