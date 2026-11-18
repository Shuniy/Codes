"""
Problem Name: String Window
Problem Difficulty: 3
Problem Constraints: Length of both the strings can be at max 10^4
Problem Description:
Ravi has been given two strings named string1 and string 2. 
He is supposed to find the minimum length substring of the string1 which contains 
all the characters of string2. Help him to find the substring

Input Format: The first line of the input contains string1. 
String1 can be a string containing spaces also.
The second line of the input contains string2. 
String2 can be a string containing spaces also.

Sample Input: qwerty asdfgh qazxsw
qas

Output Format: Output the substring in a single line. If no such substring exist then output "No String" without quotes
Sample Output: qazxs
"""
import collections

def find_minimum_substring_window(string1: str, string2: str):
	mn = float("inf")
	hashmap = collections.defaultdict(lambda: 0)
	for s in string2:
		hashmap[s] += 1

	i = 0
	total_chars = len(string2)
	result = ""

	for j in range(len(string1)):
		character = string1[j]
		if character in hashmap:
			hashmap[character] -= 1
			if hashmap[character] == 0:
				total_chars -= 1
		if total_chars == 0:
			while total_chars == 0:
				if mn > j - i + 1:
					mn = j - i + 1
					result = string1[i: j + 1]
				if string1[i]	 in hashmap:
					hashmap[string1[i]] += 1
					if hashmap[string1[i]] == 1:
						total_chars += 1
				i += 1

	return result

def main():
	string1 = str(input("Enter string1: "))
	string2 = str(input("Enter string2: "))
	print(find_minimum_substring_window(string1, string2))


main()