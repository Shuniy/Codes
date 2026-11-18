# Time : O(b + s) // small string and b is for larger string
# Space : O(b + s) // For hash table

def smallest_substring_containing(big_string, small_string):
    target_char_counts = get_char_counts(small_string)
    substring_bounds = get_substring_bounds(big_string, target_char_counts)
    return get_string_from_bounds(big_string, substring_bounds)

def get_substring_bounds(string, char_counts):
    substring_bounds = [0, float("inf")]
    substring_char_counts = {}
    num_unique_chars = len(char_counts.keys())
    num_unique_chars_done = 0
    left_index = 0
    right_index = 0
    while right_index < len(string):
        right_char = string[right_index]
        if right_char not in char_counts:
            right_index += 1
            continue
        increase_char_counts(right_char, substring_char_counts)
        if substring_char_counts[right_char] == char_counts[right_char]:
            num_unique_chars_done += 1
        while num_unique_chars_done == num_unique_chars and left_index <= right_index:
            substring_bounds = get_closer_bounds(left_index, right_index, substring_bounds[0], substring_bounds[1])
            left_char = string[left_index]
            if left_char not in char_counts:
                left_index += 1
                continue
            if substring_char_counts[left_char] == char_counts[left_char]:
                num_unique_chars_done -= 1
            decrease_char_counts(left_char, substring_char_counts)
            left_index += 1
        right_index += 1
    return substring_bounds

def get_closer_bounds(index1, index2, index3, index4):
    return [index1, index2] if index2 - index1 < index4 - index3 else [index3, index4]

def get_string_from_bounds(string, bounds):
    start, end = bounds

    if end == float('inf'):
        return ''
    return string[start: end + 1]

def get_char_counts(string):
    char_counts = {}

    for char in string:
        increase_char_counts(char, char_counts)
    return char_counts

def increase_char_counts(char, char_counts):
    if char not in char_counts:
        char_counts[char] = 0
    char_counts[char] += 1

def decrease_char_counts(char, char_counts):
    char_counts[char] -= 1
