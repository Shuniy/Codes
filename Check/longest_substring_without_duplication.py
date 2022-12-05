# Time : O(n)
# Space : O(min(N, A))

# Number of alphabets or length of string and A is the length storing as substrings

def longest_substring_without_duplication(string):
    last_seen = {}
    longest = {0, 1} # Storing indices of starting and ending
    start_index = 0

    for i, char in enumerate(string):
        if char in last_seen:
            start_index = max(start_index, last_seen[char] + 1)

        if longest[1] - longest[0] < i + 1 - start_index:
            longest = [start_index, i + 1]
        
        last_seen[char] = i

    return string[longest[0] : longest[1]]
