"""
Problem Name: Unlock
Problem Difficulty: 2
Problem Constraints: 1 <= n <= 10^5 1<= K <= 10^9

Problem Description:
Shekhar is a bomb defusal specialist. 
He once encountered a bomb that can be defused only by a secret code. 
He is given a number N and a number K. 
And he is also given permutation of first N natural numbers . 
The defusal code is the largest permutation possible by doing atmost K swaps 
among a pair of the given permutation. Help him to find the final permutation.

Input Format: First line contains an integer N and an integer k. 
The next line contains N space separated integers denoting the given permutation.

Sample Input: 5 2
3 4 1 2 6

Output Format: The final permutation of the numbers with every number separated by a space with other number.

Sample Output: 6 4 3 2 1

"""
import heapq

def find_largest_number_k_swaps(arr: list[int], n: int, k: int):
	result = arr.copy()
	index_map = {item: i for i, item in enumerate(arr)}
	maxHeap = []
	for i, item in enumerate(arr):
		heapq.heappush(maxHeap, -item)

	index = 0
	num_to_place = -heapq.heappop(maxHeap)
	while k and index < n:
		if arr[index] != num_to_place:
			current_val_index = index_map[result[index]]
			result[index], result[index_map[num_to_place]] = num_to_place, result[index]
			k -= 1
			index_map[result[index_map[num_to_place]]] = index_map[num_to_place]
			index_map[result[index]] = current_val_index

		index += 1
		num_to_place = -heapq.heappop(maxHeap)

	return result


def main():
	n = int(input("Enter size: "))
	k = int(input("Enter number of swaps k: "))
	print("Start adding numbers: ")
	arr = []
	for _ in range(n):
		arr.append(int(input()))

	print("Largest number after k swaps is: ", find_largest_number_k_swaps(arr, n, k))

main()