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
3 4 1 2 5

Output Format: The final permutation of the numbers with every number separated by a space with other number.

Sample Output: 5 4 3 2 1

"""
import collections

def find_largest_number_k_swaps_n_numbers(arr: list[int], n: int, k: int):
	result = arr.copy()
	index = 0
	num_to_place = n
	hashmap = collections.defaultdict(lambda : 0)

	for i, item in enumerate(arr):
		hashmap[item] = i

	while k and index < n:
		if arr[index] != num_to_place:
			new_index = hashmap[num_to_place]
			result[index], result[new_index] = result[new_index], result[index]
			k -= 1
			hashmap[result[new_index]] = new_index
			hashmap[result[index]] = index

		index += 1
		num_to_place -= 1

	return result

def main():
	n = int(input("Enter size: "))
	k = int(input("Enter number of swaps k: "))
	print("Start adding numbers: ")
	arr = []
	for i in range(1, n + 1):
		arr.append(i)

	print("Largest number after k swaps is: ", find_largest_number_k_swaps_n_numbers(arr, n, k))

main()
