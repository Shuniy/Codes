"""
Problem Name: String Sort
Problem Constraints: N<=1000

Problem Description:
Arvind is a very naughty boy in Launchpad Batch. 
One day he was playing with strings, and randomly shuffled them all. 
Your task is to help him Sort all the strings   ( lexicographically ) 
but if a string is present completely as a prefix in another string, 
then string with longer length should come first. 
Eg bat, batman are 2 strings and the string bat is present as a prefix in Batman - 
then sorted order should have - Batman, bat.
 
Input Format: N(integer) followed by N strings.
Sample Input: 3
bat
apple
batman

Output Format: N lines each containing one string.
Sample Output: apple
batman
bat
"""
from functools import cmp_to_key

def compare(a: str, b: str):
	prefix = ""
	i = 0
	while i < min(len(a), len(b)) and a[i] == b[i]:
		prefix += a[i]
		i += 1

	if not prefix:
		return (a > b) - (a < b)
	else:
		return len(b) - len(a)


def string_sort(arr: list[str]):
	arr.sort(key = cmp_to_key(compare))
	return arr

def main():
	print("Enter size of the array: ")
	k = int(input())
	print("Enter string values: ")
	arr = []
	for _ in range(k):
		arr.append(str(input()))
	print("Sorted array is: ", string_sort(arr))

main()