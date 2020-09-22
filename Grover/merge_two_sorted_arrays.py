"""
Given two sorted arrays x[] and y[] of size  m and n each,
merge elements of x[] with elements of array y[] by maintaining the sorted order.
i.e. fill x[] with first m smallest elements and fill y[] with remaining elements.

x = [1,4,7,8,10]
y = [2,3,9]

time = O(n*m)
space = O(1)

time can be reduced using auxillary arrays
time = O(n)
space = O(n + m)

"""

def merge(X, Y):

	m = len(X)
	n = len(Y)

	for i in range(m):
		if X[i] > Y[0]:
			temp = X[i]
			X[i] = Y[0]
			Y[0] = temp

			first = Y[0]

			k = 1
			while k < n and Y[k] < first:
				Y[k - 1] = Y[k]
				k = k + 1

			Y[k - 1] = first


if __name__ == '__main__':

	X = [1, 4, 7, 8, 10]
	Y = [2, 3, 9]

	merge(X, Y)

	print("X:", X)
	print("Y:", Y)
