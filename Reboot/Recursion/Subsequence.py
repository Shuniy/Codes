# Subsequence for String

def subsequence(string):
    output = []
    subsequenceHelper(string, 0, "", output)
    return output

def subsequenceHelper(string, i, resultString, outputArray):
    if i >= len(string):
        outputArray.append(resultString)
        return
    
    subsequenceHelper(string, i + 1, resultString + string[i], outputArray)
    subsequenceHelper(string, i + 1, resultString, outputArray)

print(subsequence("abc"))

def subsequence(arr):
    output = []
    subsequenceHelper(arr, 0, [], output)
    return output

def subsequenceHelper(arr, i, resultArray, outputArray):
    if i >= len(arr):
        outputArray.append(resultArray)
        return
    
    subsequenceHelper(arr, i + 1, resultArray + [arr[i]], outputArray)
    subsequenceHelper(arr, i + 1, resultArray, outputArray)

print(subsequence([1,2,3]))