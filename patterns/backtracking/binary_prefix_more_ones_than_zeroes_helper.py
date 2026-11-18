def prefix1Than0(n):
    output = []
    prefixHelper(n - 1, 1, 0, "1", output)
    return output

def prefixHelper(n, count1, count0, result, output):
    if n == 0:
        output.append(result)
        return
    
    if count1 > count0:
        prefixHelper(n - 1, count1 + 1, count0, result + "1", output)
        prefixHelper(n - 1, count1, count0 + 1, result + "0", output)

print(prefix1Than0(3))