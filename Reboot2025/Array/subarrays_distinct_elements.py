"""
Problem Name: Subarrays with distinct elements
Problem Difficulty: None
Problem Constraints: 1<=N<=10^5

Problem Description:
Given an array, the task is to calculate the sum of lengths of contiguous subarrays having all elements distinct

Input Format: An integer n denoting size of array followed by n integers
Sample Input: 3
1 2 3

Output Format: The answer mod 10^9+7

Sample Output: 10

arr[] = {1, 2, 1}
output = 7

arr[] = {1, 2, 3, 4}
output = 20

"""

"""
Approach 1 - Generate all the contiguous subarrays with distinct characters in it
Approach 2 - Generate just the possible subarray lengths of the array


For example:

[1,2,3]

i 	j 	max_subarray_length = j - i + 1
0 	2 	3 = [1,2,3]
1 	2 	2 = [2, 3]
2 	2 	1 = [3]

Now Sums,
[1,2,3]
i = 0, [1], [1,2], [1,2,3] = Lenghts = 1,2,3
i = 1, [2], [2, 3] = Lengths = 1,2
i = 2, [3] = Length = 1

start 	end 	max_length 		sum_of length
0 		2 		3  			6 = 1....subarray_length(j - i + 1) = 1+2+3 = N(N+2)/2
1 		2 		2 			3 = 1....subarray_length(j - i + 1) = 1+2 = N(N+2)/2
2 		2 		1 			1 = 1....subarray_length(j - i + 1) = 1 = N(N+2)/2

"""

def find_sum_subarrays_distinct_elements(arr: list[int]):
	seen = set()
	result = 0
	n = len(arr)
	j = 0
	for i in range(n):
		while j < n and arr[j] not in seen:
			seen.add(arr[j])
			j += 1
		result += (j - i + 1) * (j - i) // 2
		print(i, j, result)
		seen.remove(arr[i])

	return result

def main():
	print("Sum of subarrays of distinct elements: ", find_sum_subarrays_distinct_elements([1,2,3]))
	print("Sum of subarrays of distinct elements: ", find_sum_subarrays_distinct_elements([1,2,1]))
	print("Sum of subarrays of distinct elements: ", find_sum_subarrays_distinct_elements([1,2,3,4]))

main()
