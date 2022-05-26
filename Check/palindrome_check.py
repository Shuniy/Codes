# Time : O(n^2) Space : O(n)

def isPalindrome(string):
    reversed_string = ""
    for i in reversed(range(len(string))):
        reversed_string += string[i]
    return string == reversed_string

# Time : O(n) Space : O(n)
def isPalindrome(string):
    reversedChars = []
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])
    return string == "".join(reversedChars)

# Time : O(n) Space : O(n)
def isPalindrome(string, i = 0):
    j = len(string) - i - 1
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)

def isPalindrome(string, i = 0):
    j = len(string) - i - 1
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindrome(string, i + 1)

# Time : O(n) Space : O(1)
def isPalindrome(string):
    left_index = 0
    right_index = len(string) - 1
    while left_index < right_index:
        if string[left_index] != string[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True
