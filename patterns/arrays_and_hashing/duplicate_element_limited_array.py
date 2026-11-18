"""
Input = {1,2,3,4,5,6,4}
Output = The duplicate element is 4
"""

# Hashing can be used O(n)
# We can solve this problem in constant space. Since the array contains all distinct elements 
# exceptone and all elements lies in range 1 to n-1, we can check for duplicate element by marking
# array elements as negative by using array index as a key. For each array element arr[i], we invert
# the sign of element present at index (arr[i] - 1). Finally, we traverse array once again and if a 
# positive number is found at index i, then duplicate element is i+1.

# Above approach takes two traversals of the array. We can achieve the same in only one traversal. For 
# each array element arr[i], we invert the sign of element present ar index (arr[i] - 1) if it is positive else if
# element is already negative, then it is a duplicate.

# Function to find a duplicate element in a limited range list


def find_duplicate(arr):

	duplicate = -1

	# do for each element in the list
	for i in range(len(arr)):

		# get value of the current element
		value = -arr[i] if (arr[i] < 0) else arr[i]

		# make element at index (value-1) negative if it is positive
		if arr[value - 1] >= 0:
			arr[value - 1] = -arr[value - 1]
		else:
			# if element is already negative, it is repeated
			duplicate = value
			break

	# return duplicate element
	return duplicate


if __name__ == '__main__':

	# input list contains n numbers between [1 to n - 1]
	# with one duplicate, where n = len(arr)
	arr = [1, 2, 4, 3, 4]

	print("Duplicate element is", find_duplicate(arr))
