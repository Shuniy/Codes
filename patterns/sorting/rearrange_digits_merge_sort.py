"""
This problem, as stated to be solved in time complexity of O(n*log(n)), has given the clue to be tackled by a variation of the merge sort algorithm. Indeed, it is a merge sort algorithm, except for the particular treatment if gives to the comparison of results coming from the previous recursion, if we are on the first level of the recursion. In this case, it does the comparison, as usual, but then starts saving the results on alternative lists, which are then returned as the results.

The usage of this alternative list saving is due to the fact that having the list perfectly sorted, if we start from the index[0] and give alternatively a value to each list, occupying this value an increasing digit position, we always obtain a combination that satisfies the condition of having a maximum sum of two numbers and maximum a digit of difference between them.

Time and Space complexity
As the base of the algorithm is the merge sort, having a time complexity of O(n*log(n)), and there have been no substantial modifications to the algorithm; just the addition of O(1) operations, the time complexity remains equal. As for the space complexity, if we hold the assumption that python gets automatically rid of each previous step auxiliary created arrays, then the space complexity is of O(n) (we have always arrays tat amount to the length of the input array).

Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.
"""

def rearrange_digits(input_list: list, first_layer: bool = False) -> list:
    """
        Rearrange Array Elements so as to form two number such that their sum is maximum.
        Args:
           input_list(list): Input List
           first_layer(bool): placeholder to know if we are in the first layer of the recursion (special case)
        Returns:
           (int),(int): Two maximum sums
        """

    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]

    left = rearrange_digits(left)
    right = rearrange_digits(right)

    return merge(left, right, first_layer)


def merge(left: list, right: list, first_layer: bool = False) -> list:
    merged = []
    left_index = 0
    right_index = 0

    if first_layer:  # Special case for the last merging step
        num_max_left = ''
        num_max_right = ''
        num_to_left = True

        # Alternating between left and right indexes
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                if num_to_left:
                    num_max_left = str(right[right_index]) + num_max_left
                else:
                    num_max_right = str(right[right_index]) + num_max_right
                right_index += 1
            else:
                if num_to_left:
                    num_max_left = str(left[left_index]) + num_max_left
                else:
                    num_max_right = str(left[left_index]) + num_max_right
                left_index += 1

            num_to_left = not num_to_left  # Distribute the numbers on each of the list

        # Exhausting remaining index
        while left_index < len(left):   # left index is not exhausted
            if num_to_left:
                num_max_left = str(left[left_index]) + num_max_left
            else:
                num_max_right = str(left[left_index]) + num_max_right

            left_index += 1
            num_to_left = not num_to_left

        while right_index < len(right):  # right index is not exhausted
            if num_to_left:
                num_max_left = str(right[right_index]) + num_max_left
            else:
                num_max_right = str(right[right_index]) + num_max_right

            right_index += 1
            num_to_left = not num_to_left

        return [int(num_max_left), int(num_max_right)]

    else:  # Normal merging case
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                merged.append(right[right_index])
                right_index += 1
            else:
                merged.append(left[left_index])
                left_index += 1

        merged += left[left_index:]
        merged += right[right_index:]

        return merged

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Normal cases
print('Normal Cases:')
print('Test 1:')
list_num = [1, 2, 3, 4, 5]
result = rearrange_digits(input_list=list_num, first_layer=True)
if result == [531, 42]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 2:')
list_num = [4, 6, 2, 5, 9, 8]
result = rearrange_digits(input_list=list_num, first_layer=True)
if result == [852, 964]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 3:')
list_num = [1, 2, 3]
result = rearrange_digits(input_list=list_num, first_layer=True)
if result == [31, 2]:
    print('Pass \n')
else:
    print("Fail \n")

# Edge cases
print('Edge Cases:')
print('Test 4:')
list_num = [1, 1, 1]
result = rearrange_digits(input_list=list_num, first_layer=True)
if result == [11, 1]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 5:')
list_num = [1]
result = rearrange_digits(input_list=list_num, first_layer=True)
if result == [1]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 6:')
list_num = []
result = rearrange_digits(input_list=list_num, first_layer=True)
if result == []:
    print('Pass \n')
else:
    print("Fail \n")
