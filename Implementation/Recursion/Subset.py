# all subsets as combined called as powersets
# Subsets are just combination of elements, therefore can be generated as subsequences
# Subsets are also combinations of set, then generating all combinations will work too

def powersets(arr):
    setsize = len(arr)
    totalPowerSets = (int)(2**setsize)
    output = []
    for counter in range(0, totalPowerSets):
        string = ""
        for j in range(0, setsize):
            if counter & (1 << j):
                string += arr[j]
        
        output.append(string)
        
    return output

print(powersets(["1","2","3"]))