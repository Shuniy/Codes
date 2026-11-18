"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note:  If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input:  "Mr John Smith ", 13
Output:  "Mr%20John%20Smith"
Hints: #53, # 118
"""

# Time : O(n) : Space : O(1)
def urlify(string):
    return string.strip().replace(' ', '%20')

# Time : O(n) : Space : O(n)
def urlify(string):

    spaces = 0
    for value in string:
        if value == ' ':
            spaces += 1

    characters = [None] * (len(string) + spaces * 2)

    index = 0
    for value in string:
        if value == ' ':
            characters[index] = '%'
            characters[index + 1] = '2'
            characters[index + 2] = '0'
            index += 3
        else:
            characters[index] = value
            index += 1

    return ''.join(characters)


print(urlify("Mr  John  Smith  "))
print(urlify("Mr John Smith "))
print(urlify("13"))
