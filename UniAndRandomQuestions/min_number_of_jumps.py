# Time : O(n^2)
# Space : O(n)
def minimum_number_of_jumps(array):
    jumps = [float("inf") for i in array]

    jumps[0] = 0

    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] + j >= i:
                jumps[i] = min(jumps[j] + 1, jumps[i])

    return jumps[-1]

# Time : O(n)
# Space : O(1)

def minimum_number_of_jumps(array):
    if len(array) == 1:
        return 0

    jumps = 0
    max_reach = array[0]

    steps = array[0]

    for i in range(1, len(array) - 1):
        max_reach = max(max_reach, i + array[i])

        steps -= 1
        if steps == 0:
            jumps += 1
            steps = max_reach - i

    return jumps + 1
