"""
input = [3,-4,-7,3,1,3,1,-4,-2,-2]

Output: Subarray exists
Subarrays are:

"""
def insert(hash_table, key, value):
    hash_table.setdefault(key, []).append(value)

def print_all_sublists(arr):
    hash_table = {}

    insert(hash_table, 0, -1)

    sum = 0

    for i in range(len(arr)):
        sum += arr[i]

        if sum in hash_table:
            list = hash_table.get(sum)

            for value in list:
                print("Sublist is ", (value + 1, i))

        insert(hash_table, sum, i)

if __name__ == "__main__":
    arr = [4,-6,3,-1,4,2,7]
    print_all_sublists(arr)
