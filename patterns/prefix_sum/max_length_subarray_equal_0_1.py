"""
Given a binary array containing 0 and 1 find maximum length sub-array having equal number of 0's and 1's

Input = [0,0,1,0,1,0,0]

"""
def max_length_sublist(arr):
    hash_table = {}

    hash_table[0] = -1
    length = 0
    ending_index = -1

    sum = 0

    for i in range(len(arr)):
        sum += -1 if arr[i] == 0 else 1

        if sum in hash_table:
            if length < i - hash_table.get(sum):
                length = i - hash_table.get(sum)
                ending_index = i
        else:
            hash_table[sum] = i

    if ending_index != -1:
        print((ending_index - length + 1, ending_index))
    else:
        print("No sublist")


if __name__ == "__main__":
    arr = [0,0,1,0,1,0,0]
    max_length_sublist(arr)
