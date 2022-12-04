class Solution:
    def solve(self, s):
        result = ""
        chars = set()
        for i in range(26):
            chars.add(chr(i + 97))
        i = 0
        while i < len(s):
            count = ""
            while s[i] not in chars:
                count += s[i]
                i += 1
            count = int(count)
            while count:
                result += s[i]
                count -= 1
            i += 1
        return result


solution = Solution()
s = "4a3b2c1d2a"
print("Run Length Decoding is: ", solution.solve(s))