# Fixed Size Sliding Window

import collections


def generalFormatFixedSize():
    # initialize result
    # create a forward pointer, naming "j"
    # move that window or add the element to the window of size k
    # only two conditions are there
    # when current window size == k
    # or when current window size < k
    # if current window size is less than k, then keep adding
    # if current window size is equal to k, then compute the result
    # and then move the ith pointer, because in next step, we want to maintain the window generated
    # Now, you might need stacks or queues to store the results, as per the requirement
    # usually it uses stack and queues for harder questions but they are easy.
    
    # example below calculate first negative number in window size of k
    i: int = 0
    result: list[int] = []
    negativeNumbers: collections.deque[int] = collections.deque([item for item in arr if item < 0])
    for j in range(len(arr)):
        if j - i + 1 < k:
            continue
        else:
            if len(negativeNumbers) <= 0:
                result.append(0)
            else:
                result.append(negativeNumbers[0])
                while negativeNumbers and negativeNumbers[0] == arr[i]:
                    negativeNumbers.popleft()
                i += 1
        
    return result
    return

# Variable Size Sliding Window
def generalFormatVariableSize():
    # initialize result
    # create a forward pointer "j"
    # move that window or add keep adding the element to the window
    # there are three processes we have to follow
    # since elements will keep adding, three conditions arise
    # if result is still short of requirement,
    # we result is acquired
    # if result exceeds the requirement
    # if result is still short, keep increasing the window
    # if result is acquired, compute and process the result
    # if result is exceeded due to increased window size,
    # start decreasing the window from the left or ith pointer, untill window is under limit
    i = 0
    maxLen = float("-inf")
    hashmap = {}
    for j in range(len(string)):
        if string[j] in hashmap:
           hashmap[string[j]] += 1
        else:
            hashmap[string[j]] = 1
        if len(hashmap) < k:
            continue
        elif len(hashmap) == k:
            maxLen = max(maxLen, j - i + 1)
        else:
            while len(hashmap) > k:
                if string[i] in hashmap:
                    hashmap[string[i]] -= 1
                    if hashmap[string[i]] <= 0:
                        del hashmap[string[i]]
                i += 1
        print(i, j)
    return maxLen
    return