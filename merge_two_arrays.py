"""
Given two sorted arrays x[] and y[] of size m and n each where m >= n
and x[] has exactly n vacant cells, merge elements of y[] in their correct position in array x[] i,e. merge (x,y) by
keeping the sorted order

"""
# Function to merge X[0..m] and Y[0..n] to X[0..m+n+1]


def merge(X, Y, m, n):
	k = m + n + 1

	while m >= 0 and n >= 0:
		if X[m] > Y[n]:
			X[k] = X[m]
			m = m - 1
		else:
			X[k] = Y[n]
			n = n - 1
		k = k - 1

	while n >= 0:
		X[k] = Y[n]
		k = k - 1
		n = n - 1

def rearrange(X, Y):

	k = 0
	for i in range(len(X)):
		if X[i]:
			X[k] = X[i]
			k = k + 1

	merge(X, Y, k - 1, len(Y) - 1)


if __name__ == '__main__':

	# vacant cells in X is represented by 0
	X = [0, 2, 0, 3, 0, 5, 6, 0, 0]
	Y = [1, 8, 9, 10, 15]

	rearrange(X, Y)
	print(X)
