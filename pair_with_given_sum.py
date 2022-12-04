# Three methods are possible
# Two Loops
# Using sorting
# Using hashing

"""
arr = [8,7,2,5,3,1]
sum = 10

Output
Pair found at index 0 and 2 (8 + 2)
Pair found at index 1 and 4 (7 + 3)
"""
def find_pair(arr, sum):
    hash_table = {}

    for i, element in enumerate(arr):
        if sum - element in hash_table:
            print("Pair found at index ", hash_table.get(sum - element), "and ", i)
        hash_table[element] = i
    hash_table[element] = i
if __name__ == "__main__":
    arr = [8, 7, 2, 5, 3, 1]
    sum = 10
    find_pair(arr, sum)
