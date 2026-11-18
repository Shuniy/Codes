import math

"""
Problem Statement
You are given a non-negative number in the form of list elements. For example, the number 123 would be provided as arr = [1, 2, 3].
Add one to the number and return the output in the form of a new list.

Example 1:

input = [1, 2, 3]
output = [1, 2, 4]
Example 2:

input = [9, 9, 9]
output = [1, 0, 0, 0]
Challenge:

One way to solve this problem is to convert the input array into a number and then add one to it. 
For example, if we have input = [1, 2, 3], you could solve this problem by creating the number 123 and then separating the digits of the output number 124.
"""
def listToString(input_list : list) -> str:
    string = str()
    for i in input_list:
        string += str(i)
    return string

def stringAddOne(string : str) -> str:
    number = int(string)
    number += 1
    return str(number)

def stringToList(string : str) -> list:
    return [int(char) for char in string]


def addOne(input_list : list) -> list:
    return stringToList(stringAddOne(listToString(input_list)))


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = addOne(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")


arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)

"""
Approach : To add one to number represented by digits, follow the below steps :

Parse the given array from end like we do in school addition.
If the last elements 9, make it 0 and carry = 1.
For the next iteration check carry and if it adds to 10, do same as step 2.
After adding carry, make carry = 0 for the next iteration.
If the vectors add and increase the vector size, append 1 in the beginning.
"""

def AddOne(input_list : list) -> list:
    n = len(input_list)
    input_list[n - 1] += 1
    carry = input_list[n - 1] / 10
    input_list[n - 1] = input_list[n - 1] % 10

    for i in range(n - 2, -1, -1):
        if carry == 1:
            input_list[i] += 1
            carry = input_list[i] / 10
            input_list[i] = input_list[i] % 10

    if carry == 1:
        input_list.insert(0, 1)
    return input_list
