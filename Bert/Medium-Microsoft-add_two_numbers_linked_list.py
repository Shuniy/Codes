"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Here is the function signature as a starting point (in Python):

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print result.val,
  result = result.next
# 7 0 8
"""
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        # Fill this in.
        head = result = ListNode(0)
        while l1 or l2:
            l1.val = l1.val if l1 else 0
            l2.val = l2.val if l2 else 0

            digit_sum = l1.val + l2.val

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            result.val = digit_sum
            result.next = ListNode(c) if l1 or l2 or c else None
            result = result.next
        return head


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
