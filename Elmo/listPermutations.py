import copy

def permute(input):
    if len(input) <= 1:
        return [input]
    elif len(input) == 2:
        return [input, input[::-1]]
    else:
        output = []
        currentLevel = input[0]
        previousLevel = permute(input[1:])

        for element in previousLevel:
            for position in range(len(element) + 1):
                tempList = []
                temp = element.copy()
                for i in range(len(element) + 1):
                    if position == i:
                        tempList.append(currentLevel)
                    else:
                        tempList.append(temp.pop())
                output.append(tempList)
    return output

def check_output(output, expected_output):
    o = copy.deepcopy(output)
    e = copy.deepcopy(expected_output)
    o.sort()
    e.sort()
    return o == e


print("Pass" if (check_output(permute([]), [[]])) else "Fail")
print("Pass" if (check_output(permute([0]), [[0]])) else "Fail")
print("Pass" if (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print("Pass" if (check_output(permute([0, 1, 2]), [[0, 1, 2], [
      0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")
