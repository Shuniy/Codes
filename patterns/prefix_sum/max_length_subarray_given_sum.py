"""
Given an array of integers, find maximum length sub-array having given sum

arr = [5,6,-5,5,3,5,3,-2,0]
sum = 8
"""
# Using loops can lead to O(n^3)
# Using map will solve it in O(n)

def maxLengthSubList(A, S):

	dict = {}

	# insert (0, -1) pair into the set to handle the case when
	# sublist with sum S starts from index 0
	dict[0] = -1
	sum = 0

	length = 0
	ending_index = -1

	for i in range(len(A)):
		sum += A[i]

		if sum not in dict:
			dict[sum] = i

		if sum - S in dict and length < i - dict[sum - S]:
			length = i - dict[sum - S]
			ending_index = i

	print((ending_index - length + 1, ending_index))


if __name__ == '__main__':

	A = [5, 6, -5, 5, 3, 5, 3, -2, 0]
	sum = 8

	maxLengthSubList(A, sum)
