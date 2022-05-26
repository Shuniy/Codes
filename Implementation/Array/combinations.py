# Combinations -> nC1, nC2, nC3.........nCn
def combination(arr):
    if not arr:
        return [[]]
        
    firstElement = arr[0]
    restElementsCombo = combination(arr[1:])
    
    comboWithFirstElement = []
    
    for combo in restElementsCombo:
        comboWithFirstElement.append(combo + [firstElement])
        
    return restElementsCombo + comboWithFirstElement

# Combination with repetition is not actually thing, but if considered might be similar to 
# permutation with repetiton
def combinationWithRepetitionHelper(arr, currentIndex, outcome):
    for i in range(currentIndex, len(arr)):
        outcome[currentIndex] = arr[i]
        
        if currentIndex == len(arr) - 1:
            print(outcome)
        else:
            combinationWithRepetitionHelper(arr, currentIndex + 1, outcome)
        
def combinationWithRepetion(arr):
    combinationWithRepetitionHelper(arr, 0, [None for _ in range(len(arr))])

# Combination with repetition with k elemenets
def combinationWithRepetionWithKHelper(arr, k, output):
    if len(output) == k:
        print(output)
        return
    
    for i in range(len(arr)):
        output.append(arr[i])
        combinationWithRepetionWithKHelper(arr, k, output)
        output.pop()

def combinationWithRepetionWithK(arr, k):
    combinationWithRepetionWithKHelper(arr, k, [])


arr = [1,2,3]
print("Combinations : ")
print(combination(arr))
print("Combinations with Repetitions")
combinationWithRepetion(arr)
print("Combination with repetition with k elements : ")
k = 2
combinationWithRepetionWithK(arr, k)