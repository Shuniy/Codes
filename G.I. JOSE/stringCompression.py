"""
String Compression: Implement a method to perform basic string compression using the counts
of  repeated  characters.  For  example,  the  string aabcccccaaa  would become  a2blc5a3.  If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
Hints:#92, #110
"""

# Time : O(n) | O(nlogn) : Space : O(n)
def stringCompression(string):
    if not string:
        return string

    hashmap = dict()

    for item in string:
        if item in hashmap:
            hashmap[item] += 1
        else:
            hashmap[item] = 1

    string = ''
    for key, value in sorted(hashmap.items(), key = lambda x : x[0]):
        if value == 1:
            string += key
        else:
            string += key + str(value)

    return string

# However we want a different kind of Compression, which is easy to Implement
# Time : O(n) : Space : O(n) | O(1) depends on string since we cant change initial string
def stringCompression(string):
    if not string:
        return string

    count = 1
    result = ''
    for i in range(1, len(string)):
        if string[i] != string[i - 1]:
            result += string[i - 1] + str(count)
            count = 1
        else:
            count += 1
        if i == len(string) - 1:
            result += string[i] + str(count)

    return result if len(result) < len(string) * 2 else string

print(stringCompression('aabcccccaaa'))
print(stringCompression('abcd'))
