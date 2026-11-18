def sortStackRecursion(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    topElement = arr.pop()
    restSortedStack = sortStackRecursion(arr)
    return findCorrectPlace(topElement, restSortedStack)

def findCorrectPlace(element: int, arr: list[int]) -> list[int]:
    if len(arr) <= 0:
        return [element]
    
    topElement = arr.pop()
    if topElement <= element:
        arr.append(topElement)
        arr.append(element)
        return arr
    else:
        result = findCorrectPlace(element, arr)
        result.append(topElement)
        return result

arr = [9,8,7,6,5,4,3,2,1,10]
print("Sorted Stack", sortStackRecursion(arr))