# Naive
# Time : O(n^3) // Not using exaclty dynammic programming
# Space : O(n^2)

def palindrome_partitioning_min_cuts(string):
    palindromes = [[False for i in string] for _ in string]

    for i in range(len(string)):
        for j in range(i, len(string)):
            palindromes[i][j] = is_palindrome(string[i : j+1])

    cuts = [float('inf') for _ in string]
    for i in range(len(string)):
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = cuts[i - 1] + 1
            for j in range(1, i):
                if palindromes[j][i] and cuts[j - 1] + 1 < cuts[i]:
                    # cuts[i] = min(cuts[i], cuts[j - 1] + 1)
                    cuts[i] = cuts[j - 1] + 1

    return cuts[-1]

def is_palindrome(string):
    left_index = 0
    right_index = len(string) - 1
    
    while left_index < right_index:
        if string[left_index] != string[right_index]:
            return False
        left_index += 1
        right_index -=1
    return True 

# Optimal
# Time : O(n^2) // Dynamminc Programming
# Space : O(n^2)

def palindrome_partitioning_min_cuts(string):
    palindromes = [[False for i in string] for _ in string]

    for i in range(len(string)):
        palindromes[i][i] = True

    for length in range(2, len(string) + 1):
        for i in range(0, len(string) - length + 1):
            j = i + length - 1
            if length == 2:
                palindromes[i][j] = string[i] == string[j]
            else:
                palindromes[i][j] = string[i] == string[j] and palindromes[i + 1][j + 1]

    cuts = [float('inf') for _ in string]
    for i in range(len(string)):
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = cuts[i - 1] + 1
            for j in range(1, i):
                if palindromes[j][i] and cuts[j - 1] + 1 < cuts[i]:
                    # cuts[i] = min(cuts[i], cuts[j - 1] + 1)
                    cuts[i] = cuts[j - 1] + 1

    return cuts[-1]
