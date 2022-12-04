"""
Given a string, find the length of the longest substring without repeating characters.

Here is an example solution in Python language. (Any language is OK to use in an interview, though we'd recommend Python as a generalist language utilized by companies like Google, Facebook, Netflix, Dropbox, Pinterest, Uber, etc.,)

class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.

print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10

Can you find a solution in linear time?

Sliding Window Problem
"""

from collections import deque

class Solution:
    def lengthofLongestSubstring(self, s):
        appearedChar = dict()
        start = 0
        end = 0
        seq_pair = []
        seq_length = []

        for i, currentChar in enumerate(s):
            if currentChar not in appearedChar:
                appearedChar[currentChar] = i
                end = i
            else:
                if currentChar == s[i - 1]:
                    start = i
                    end = i
                    appearedChar.clear()
                    appearedChar[currentChar] = i
                else:
                    start = appearedChar[currentChar] + 1
                    end = i
                    appearedChar = {k : v for k, v in appearedChar.iteritems() if v >= start}
                    appearedChar[currentChar] = i
                seq_pair.append((start, end))
                seq_length.append(end - start + 1)
        return max(seq_length) if seq_length else 0


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
