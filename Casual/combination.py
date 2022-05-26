
def combinations(arr):
    if len(arr) == 0:
        return [[]]
    
    comboWithFirst = []
    firstElement = arr[0]
    restElementsCombo = combinations(arr[1:])
    
    for element in restElementsCombo:
        comboWithFirst.append([firstElement] + element)
        
    return comboWithFirst + restElementsCombo
    
result = []
arr = [1,2,3]
print(combinations(arr))

