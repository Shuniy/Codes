# Substring Matching mainly used in DNA sequencing and repeated substrings
# Naive two for loops : Time : O(n * m)

# Time : O(n + m) // n longest substring and m substring to match
# Space : O(m)

def knutt_morris_pratt(string, substring):
    pattern = build_pattern(substring)
    return does_match(string, substring, pattern)

# Time : O(m)
# Space : O(m)
def build_pattern(substring):
    pattern = [-1 for i in substring]
    j = 0
    i = 1

    while i < len(substring):
        if substring[i] == substring[j]:
            pattern[i] = j
            i += 1
            j += 1
        elif j > 0: 
            j = pattern[j - 1] + 1
        else:
            i += 1

    return pattern

# Time : O(n)
# Space : O(1)
def does_match(string, substring, pattern):
    i = 0
    j = 0
    while i + len(substring) - j <= len(string):
        if string[i] == substring[j]:
            if j == len(substring) - 1:
                return True
            else:
                i += 1
                j += 1
        elif j > 0:
            j = pattern[j - 1] + 1

    # If want the index where the pattern started just subtract len(substring) with i
    return False
