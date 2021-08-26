"""
Given an integer k and a string s, find the length of the longest substring
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct
characters is "bcb".
"""

def get_longest_sub_with_k_dist(string, k):
    if not string:
        return ""
    elif len(string) <= k:
        return string
    elif k == 1:
        return string[0]

    distinct_char_count = 0
    seen_chars = set()
    candidate = None
    remaining_string = None

    first_char = string[0]
    second_char_index = 0
    while string[second_char_index] == first_char:
        second_char_index += 1

    candidate = string
    for index, char in enumerate(string):
        if char not in seen_chars:
            seen_chars.add(char)
            distinct_char_count += 1
        if distinct_char_count > k:
            candidate = string[:index]
            remaining_string = string[second_char_index:]
            break
    longest_remaining = get_longest_sub_with_k_dist(remaining_string, k)
    longest_substring = None

    if len(candidate) < len(longest_remaining):
        longest_substring = longest_remaining
    else:
        longest_substring = candidate
    return longest_substring

assert get_longest_sub_with_k_dist("abcba", 2) == "bcb"
assert get_longest_sub_with_k_dist("abccbba", 2) == "bccbb"
assert get_longest_sub_with_k_dist("abcbbbabbcbbadd", 2) == "bbbabb"
assert get_longest_sub_with_k_dist("abcbbbaaaaaaaaaabbcbbadd", 1) == "a"
assert get_longest_sub_with_k_dist("abccbba", 3) == "abccbba"
