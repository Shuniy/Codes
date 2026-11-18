def substrings(string):
    output = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            output.append(string[i: j + 1])
    
    return output

print(substrings("abc"))

def substrings(string):
    output = []
    substringsHelper(string, 0, 0, output)
    return output

def substringsHelper(string, start, end, output):
    if end > len(string):
        return
    
    if start > end:
        substringsHelper(string, 0, end + 1, output)
        return
    
    output.append(string[start: end])
    substringsHelper(string, start + 1, end, output)
    

print(substrings("abc"))