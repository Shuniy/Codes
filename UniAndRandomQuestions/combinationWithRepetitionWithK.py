
def combinationWithRepetitionHelper(arr, n, k, output, currentIndex):
    
    if len(output) == k:
        result.append(output[:])
        return
    
    for i in range(currentIndex, n):
        output.append(arr[i])
        combinationWithRepetitionHelper(arr, n, k, output, i)
        output.pop()

def combinationWithRepetition(arr, k):
    combinationWithRepetitionHelper(arr, len(arr), k, [], 0)

result = []
arr = [1,2,3]
k = 2
combinationWithRepetition(arr, k)
print(result)